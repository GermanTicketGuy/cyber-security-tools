#!/usr/bin/env python3
"""Generate README.md from the TOML data files.

Data lives in `data/*.toml` (one file per category) and the category order /
metadata lives in `categories.toml`. Run `python3 generate.py` to rewrite
README.md. Run `python3 generate.py --check` to additionally query the GitHub
API and warn about forks (we only ever link the original repo), archived repos
and dead links. Set GITHUB_TOKEN in the environment for a higher rate limit.
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
CATEGORIES_FILE = ROOT / "categories.toml"
README_FILE = ROOT / "README.md"

SHIELDS = "https://img.shields.io/github"
GITHUB_URL = "https://github.com"


def load_toml(path: Path) -> dict:
    with path.open("rb") as fh:
        return tomllib.load(fh)


def slugify_repo(repo: str) -> str:
    """Normalise a repo reference to `owner/name`."""
    repo = repo.strip()
    for prefix in ("https://github.com/", "http://github.com/", "github.com/"):
        if repo.startswith(prefix):
            repo = repo[len(prefix):]
    return repo.rstrip("/").removesuffix(".git")


def gh_anchor(text: str) -> str:
    """Replicate GitHub's heading-anchor algorithm.

    Lowercase, drop everything that is not a letter, number, space or hyphen
    (this removes '&', parentheses, emoji, …), then turn spaces into hyphens.
    Consecutive spaces are NOT collapsed — GitHub keeps them, so "A & B" -> "a--b".
    """
    kept = [ch for ch in text.lower() if ch.isalnum() or ch in " -"]
    return "".join(kept).replace(" ", "-")


def stars_badge(repo: str) -> str:
    return f"![Stars]({SHIELDS}/stars/{repo}?style=flat&label=&color=444)"


def updated_badge(repo: str) -> str:
    return f"![Last commit]({SHIELDS}/last-commit/{repo}?style=flat&label=&color=555)"


def build_readme(categories: list[dict], tools_by_cat: dict[str, list[dict]]) -> str:
    total_tools = sum(len(v) for v in tools_by_cat.values())
    total_cats = len([c for c in categories if tools_by_cat.get(c["slug"])])

    lines: list[str] = []
    a = lines.append

    # --- Header -------------------------------------------------------------
    a("# Awesome Security Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    a("")
    a("> A curated, always-up-to-date arsenal of open-source cyber security tools —")
    a("> from OSINT and reconnaissance to malware analysis, red teaming and DFIR.")
    a("")
    a("Every entry links to the **original project** (never a fork), and the badges")
    a("below each tool show live star counts and the last commit, so you can tell at a")
    a("glance what is actively maintained.")
    a("")
    a(f"**{total_tools} tools** across **{total_cats} categories** · "
      "Found something missing? [Add a tool »](CONTRIBUTING.md)")
    a("")
    a("---")
    a("")

    # --- Table of contents --------------------------------------------------
    a("## Contents")
    a("")
    for cat in categories:
        tools = tools_by_cat.get(cat["slug"])
        if not tools:
            continue
        anchor = gh_anchor(cat["name"])
        emoji = cat.get("emoji", "")
        prefix = f"{emoji} " if emoji else ""
        a(f"- [{prefix}{cat['name']}](#{anchor}) ({len(tools)})")
    a("")
    a("---")
    a("")

    # --- Categories ---------------------------------------------------------
    for cat in categories:
        tools = tools_by_cat.get(cat["slug"])
        if not tools:
            continue
        # Emoji is intentionally kept out of the heading so the GitHub anchor is
        # predictable; it still appears in the table of contents above.
        a(f"## {cat['name']}")
        a("")
        if cat.get("description"):
            a(f"*{cat['description']}*")
            a("")
        a("| Tool | Stars | Last commit | Description |")
        a("| --- | --- | --- | --- |")
        for tool in sorted(tools, key=lambda t: t["name"].lower()):
            repo = slugify_repo(tool["repo"])
            name_cell = f"**[{tool['name']}]({GITHUB_URL}/{repo})**"
            desc = tool.get("description", "").strip().replace("|", "\\|")
            a(f"| {name_cell} | {stars_badge(repo)} | {updated_badge(repo)} | {desc} |")
        a("")
        a("[⬆ Back to top](#contents)")
        a("")

    a("---")
    a("")
    a("## Contributing")
    a("")
    a("This list is generated from the TOML files in [`data/`](data/). "
      "Do **not** edit `README.md` by hand — edit the data and run `python3 generate.py`. "
      "See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.")
    a("")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------
# Optional GitHub API validation (--check)
# --------------------------------------------------------------------------

def _ssl_context() -> ssl.SSLContext:
    """Verified context, falling back to unverified if the local Python has no
    CA bundle (common with python.org builds that never ran Install Certificates).
    CI runs on a properly configured machine, so verification holds there."""
    ctx = ssl.create_default_context()
    try:
        ctx.load_default_certs()
        if ctx.get_ca_certs():
            return ctx
    except Exception:  # noqa: BLE001
        pass
    print("  ℹ️  No CA bundle found locally — skipping TLS verification for this run.")
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


_SSL_CTX: ssl.SSLContext | None = None


def github_get(repo: str) -> dict | None:
    global _SSL_CTX
    if _SSL_CTX is None:
        _SSL_CTX = _ssl_context()
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-security-generator"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15, context=_SSL_CTX) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as exc:
        print(f"  ⚠️  {repo}: HTTP {exc.code} ({exc.reason})")
        return None
    except Exception as exc:  # noqa: BLE001
        print(f"  ⚠️  {repo}: {exc}")
        return None


def check_repos(tools_by_cat: dict[str, list[dict]]) -> int:
    problems = 0
    seen: set[str] = set()
    for tools in tools_by_cat.values():
        for tool in tools:
            repo = slugify_repo(tool["repo"])
            if repo in seen:
                continue
            seen.add(repo)
            info = github_get(repo)
            if info is None:
                problems += 1
                continue
            if info.get("fork"):
                parent = (info.get("parent") or {}).get("full_name", "?")
                print(f"  🍴 {repo} is a FORK — link the original instead: {parent}")
                problems += 1
            if info.get("archived"):
                print(f"  📦 {repo} is ARCHIVED (no longer maintained)")
    if not problems:
        print("  ✅ All repos look good (originals, not archived).")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate README.md from data/")
    parser.add_argument("--check", action="store_true",
                        help="query GitHub API for forks / archived / dead links")
    args = parser.parse_args()

    categories = load_toml(CATEGORIES_FILE)["category"]

    tools_by_cat: dict[str, list[dict]] = {}
    known_slugs = {c["slug"] for c in categories}
    for data_file in sorted(DATA_DIR.glob("*.toml")):
        slug = data_file.stem
        if slug not in known_slugs:
            print(f"⚠️  {data_file.name}: no matching category in categories.toml", file=sys.stderr)
        data = load_toml(data_file)
        tools_by_cat[slug] = data.get("tool", [])

    readme = build_readme(categories, tools_by_cat)
    README_FILE.write_text(readme, encoding="utf-8")
    total = sum(len(v) for v in tools_by_cat.values())
    print(f"✅ Wrote {README_FILE.name} — {total} tools in {len(tools_by_cat)} categories.")

    if args.check:
        print("\n🔎 Checking repos against the GitHub API…")
        problems = check_repos(tools_by_cat)
        if problems:
            print(f"\n{problems} issue(s) found.")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
