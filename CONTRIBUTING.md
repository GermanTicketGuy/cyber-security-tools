# Contributing

Thanks for helping build the list! The `README.md` is **generated** — never edit
it by hand. You only ever touch the data files.

## Add a tool

1. Find the right category file in [`data/`](data/) (e.g. `data/osint.toml`).
   Need a new category? Add a block to [`categories.toml`](categories.toml) and
   create a matching `data/<slug>.toml`.
2. Add an entry at the bottom of the file:

   ```toml
   [[tool]]
   name = "Nmap"
   repo = "nmap/nmap"
   description = "The classic network discovery and security auditing scanner."
   ```

   - **`name`** — how the tool is commonly known.
   - **`repo`** — `owner/name` of the **original** GitHub repository. Full URLs
     work too; they get normalised.
   - **`description`** — one clear sentence. No trailing period preference, but
     keep it short.

3. Regenerate and validate:

   ```bash
   python3 generate.py --check
   ```

4. Commit both your data change **and** the regenerated `README.md`.

## The golden rule: link the original, not a fork

This list always points to the **project of origin** — the initial `nmap/nmap`,
not someone's fork. `python3 generate.py --check` queries the GitHub API and will
warn you if a repo is a fork (and tell you the parent to use instead) or if it is
archived. Set a `GITHUB_TOKEN` environment variable to avoid API rate limits:

```bash
export GITHUB_TOKEN=ghp_xxx
python3 generate.py --check
```

## Requirements

- Python 3.11+ (uses the built-in `tomllib`). No third-party packages needed.
- Sort within a category is automatic (alphabetical) — add entries anywhere.
