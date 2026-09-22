# Cyber Security Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, always-up-to-date arsenal of open-source cyber security tools —
> from OSINT and reconnaissance to malware analysis, red teaming and DFIR.

Every entry links to the **original project** (never a fork), and the badges
below each tool show live star counts and the last commit, so you can tell at a
glance what is actively maintained.

**93 tools** across **18 categories** · Found something missing? [Add a tool »](CONTRIBUTING.md)

---

## Contents

- [🔎 OSINT](#osint) (6)
- [🛰️ Reconnaissance & Attack Surface](#reconnaissance--attack-surface) (6)
- [📡 Network Scanning](#network-scanning) (5)
- [🕸️ Web Application Security](#web-application-security) (6)
- [💥 Exploitation & Red Team](#exploitation--red-team) (6)
- [🎛️ Command & Control (C2)](#command--control-c2) (5)
- [🔑 Password Attacks & Wordlists](#password-attacks--wordlists) (5)
- [📶 Wireless & Network Attacks](#wireless--network-attacks) (5)
- [🧬 Reverse Engineering](#reverse-engineering) (5)
- [🦠 Malware Analysis](#malware-analysis) (5)
- [🕵️ Digital Forensics & DFIR](#digital-forensics--dfir) (5)
- [🌐 Threat Intelligence](#threat-intelligence) (5)
- [🛡️ Detection & Blue Team](#detection--blue-team) (5)
- [🧱 Hardening & Defense](#hardening--defense) (4)
- [☁️ Cloud & Container Security](#cloud--container-security) (5)
- [📱 Mobile Security](#mobile-security) (5)
- [🩹 Vulnerability Scanning](#vulnerability-scanning) (5)
- [🎯 CTF & Training](#ctf--training) (5)

---

## OSINT

*Open-source intelligence: gather public data on people, domains and infrastructure.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[GHunt](https://github.com/mxrch/GHunt)** | ![Stars](https://img.shields.io/github/stars/mxrch/GHunt?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/mxrch/GHunt?style=flat&label=&color=555) | Investigates Google accounts and their public traces (Maps, Calendar, etc.). |
| **[holehe](https://github.com/megadose/holehe)** | ![Stars](https://img.shields.io/github/stars/megadose/holehe?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/megadose/holehe?style=flat&label=&color=555) | Checks whether an email address is registered on 120+ websites. |
| **[Maigret](https://github.com/soxoj/maigret)** | ![Stars](https://img.shields.io/github/stars/soxoj/maigret?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/soxoj/maigret?style=flat&label=&color=555) | Collects a person's dossier by username from thousands of sites. |
| **[Sherlock](https://github.com/sherlock-project/sherlock)** | ![Stars](https://img.shields.io/github/stars/sherlock-project/sherlock?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/sherlock-project/sherlock?style=flat&label=&color=555) | Hunts down social-media accounts by username across hundreds of sites. |
| **[SpiderFoot](https://github.com/smicallef/spiderfoot)** | ![Stars](https://img.shields.io/github/stars/smicallef/spiderfoot?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/smicallef/spiderfoot?style=flat&label=&color=555) | Automates OSINT collection to map a target's attack surface from 200+ sources. |
| **[theHarvester](https://github.com/laramies/theHarvester)** | ![Stars](https://img.shields.io/github/stars/laramies/theHarvester?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/laramies/theHarvester?style=flat&label=&color=555) | Gathers emails, names, subdomains and hosts from public sources. |

[⬆ Back to top](#contents)

## Reconnaissance & Attack Surface

*Subdomain discovery, asset enumeration and mapping an external attack surface.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Amass](https://github.com/owasp-amass/amass)** | ![Stars](https://img.shields.io/github/stars/owasp-amass/amass?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/owasp-amass/amass?style=flat&label=&color=555) | In-depth attack-surface mapping and asset discovery by the OWASP project. |
| **[httpx](https://github.com/projectdiscovery/httpx)** | ![Stars](https://img.shields.io/github/stars/projectdiscovery/httpx?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/projectdiscovery/httpx?style=flat&label=&color=555) | Fast and multi-purpose HTTP toolkit for probing live web servers. |
| **[Naabu](https://github.com/projectdiscovery/naabu)** | ![Stars](https://img.shields.io/github/stars/projectdiscovery/naabu?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/projectdiscovery/naabu?style=flat&label=&color=555) | Fast port scanner focused on reliability and simplicity for recon pipelines. |
| **[reconftw](https://github.com/six2dez/reconftw)** | ![Stars](https://img.shields.io/github/stars/six2dez/reconftw?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/six2dez/reconftw?style=flat&label=&color=555) | Automated reconnaissance framework chaining dozens of recon tools. |
| **[Subfinder](https://github.com/projectdiscovery/subfinder)** | ![Stars](https://img.shields.io/github/stars/projectdiscovery/subfinder?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/projectdiscovery/subfinder?style=flat&label=&color=555) | Fast passive subdomain discovery using many public sources. |
| **[Sublist3r](https://github.com/aboul3la/Sublist3r)** | ![Stars](https://img.shields.io/github/stars/aboul3la/Sublist3r?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/aboul3la/Sublist3r?style=flat&label=&color=555) | Enumerates subdomains using search engines and public data. |

[⬆ Back to top](#contents)

## Network Scanning

*Port scanners and host discovery for auditing networks at any scale.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[AngryIP Scanner](https://github.com/angryip/ipscan)** | ![Stars](https://img.shields.io/github/stars/angryip/ipscan?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/angryip/ipscan?style=flat&label=&color=555) | Fast, cross-platform IP address and port scanner with a simple GUI. |
| **[Masscan](https://github.com/robertdavidgraham/masscan)** | ![Stars](https://img.shields.io/github/stars/robertdavidgraham/masscan?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/robertdavidgraham/masscan?style=flat&label=&color=555) | Internet-scale port scanner able to scan the whole IPv4 range quickly. |
| **[Nmap](https://github.com/nmap/nmap)** | ![Stars](https://img.shields.io/github/stars/nmap/nmap?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/nmap/nmap?style=flat&label=&color=555) | The classic network discovery and security auditing scanner. |
| **[RustScan](https://github.com/bee-san/RustScan)** | ![Stars](https://img.shields.io/github/stars/bee-san/RustScan?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/bee-san/RustScan?style=flat&label=&color=555) | Modern port scanner that feeds open ports straight into Nmap. |
| **[ZMap](https://github.com/zmap/zmap)** | ![Stars](https://img.shields.io/github/stars/zmap/zmap?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/zmap/zmap?style=flat&label=&color=555) | Fast single-packet network scanner designed for Internet-wide surveys. |

[⬆ Back to top](#contents)

## Web Application Security

*Scanners, fuzzers and proxies for finding flaws in web applications and APIs.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[ffuf](https://github.com/ffuf/ffuf)** | ![Stars](https://img.shields.io/github/stars/ffuf/ffuf?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/ffuf/ffuf?style=flat&label=&color=555) | Fast web fuzzer for content discovery, parameters and virtual hosts. |
| **[Nikto](https://github.com/sullo/nikto)** | ![Stars](https://img.shields.io/github/stars/sullo/nikto?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/sullo/nikto?style=flat&label=&color=555) | Web server scanner that checks for thousands of dangerous files and misconfigs. |
| **[Nuclei](https://github.com/projectdiscovery/nuclei)** | ![Stars](https://img.shields.io/github/stars/projectdiscovery/nuclei?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/projectdiscovery/nuclei?style=flat&label=&color=555) | Template-based vulnerability scanner powered by a huge community ruleset. |
| **[OWASP ZAP](https://github.com/zaproxy/zaproxy)** | ![Stars](https://img.shields.io/github/stars/zaproxy/zaproxy?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/zaproxy/zaproxy?style=flat&label=&color=555) | Full-featured open-source web application security scanner and proxy. |
| **[sqlmap](https://github.com/sqlmapproject/sqlmap)** | ![Stars](https://img.shields.io/github/stars/sqlmapproject/sqlmap?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/sqlmapproject/sqlmap?style=flat&label=&color=555) | Automates detection and exploitation of SQL injection flaws. |
| **[Wfuzz](https://github.com/xmendez/wfuzz)** | ![Stars](https://img.shields.io/github/stars/xmendez/wfuzz?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/xmendez/wfuzz?style=flat&label=&color=555) | Web application fuzzer for brute-forcing parameters, directories and forms. |

[⬆ Back to top](#contents)

## Exploitation & Red Team

*Frameworks and tooling for offensive operations and adversary simulation.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[BloodHound](https://github.com/SpecterOps/BloodHound)** | ![Stars](https://img.shields.io/github/stars/SpecterOps/BloodHound?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/SpecterOps/BloodHound?style=flat&label=&color=555) | Reveals hidden attack paths in Active Directory using graph analysis. |
| **[Impacket](https://github.com/fortra/impacket)** | ![Stars](https://img.shields.io/github/stars/fortra/impacket?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/fortra/impacket?style=flat&label=&color=555) | Python classes for working with network protocols; a red-team staple. |
| **[Metasploit Framework](https://github.com/rapid7/metasploit-framework)** | ![Stars](https://img.shields.io/github/stars/rapid7/metasploit-framework?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/rapid7/metasploit-framework?style=flat&label=&color=555) | The de facto framework for developing and executing exploits. |
| **[NetExec](https://github.com/Pennyw0rth/NetExec)** | ![Stars](https://img.shields.io/github/stars/Pennyw0rth/NetExec?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/Pennyw0rth/NetExec?style=flat&label=&color=555) | Network exec tool (the maintained successor to CrackMapExec) for AD pentesting. |
| **[PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)** | ![Stars](https://img.shields.io/github/stars/swisskyrepo/PayloadsAllTheThings?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/swisskyrepo/PayloadsAllTheThings?style=flat&label=&color=555) | A vast collection of payloads and bypass techniques for web and AD attacks. |
| **[Responder](https://github.com/lgandx/Responder)** | ![Stars](https://img.shields.io/github/stars/lgandx/Responder?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/lgandx/Responder?style=flat&label=&color=555) | LLMNR/NBT-NS/mDNS poisoner for capturing credentials on a network. |

[⬆ Back to top](#contents)

## Command & Control (C2)

*Post-exploitation command-and-control frameworks for red teams.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Covenant](https://github.com/cobbr/Covenant)** | ![Stars](https://img.shields.io/github/stars/cobbr/Covenant?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/cobbr/Covenant?style=flat&label=&color=555) | .NET command-and-control framework for red-team operations. |
| **[Havoc](https://github.com/HavocFramework/Havoc)** | ![Stars](https://img.shields.io/github/stars/HavocFramework/Havoc?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/HavocFramework/Havoc?style=flat&label=&color=555) | Modern, malleable post-exploitation command-and-control framework. |
| **[Merlin](https://github.com/Ne0nd0g/merlin)** | ![Stars](https://img.shields.io/github/stars/Ne0nd0g/merlin?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/Ne0nd0g/merlin?style=flat&label=&color=555) | Cross-platform post-exploitation C2 server built on HTTP/2. |
| **[Mythic](https://github.com/its-a-feature/Mythic)** | ![Stars](https://img.shields.io/github/stars/its-a-feature/Mythic?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/its-a-feature/Mythic?style=flat&label=&color=555) | Collaborative, multi-agent red-team C2 framework with a web UI. |
| **[Sliver](https://github.com/BishopFox/sliver)** | ![Stars](https://img.shields.io/github/stars/BishopFox/sliver?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/BishopFox/sliver?style=flat&label=&color=555) | Open-source, cross-platform adversary emulation and C2 framework. |

[⬆ Back to top](#contents)

## Password Attacks & Wordlists

*Password cracking, credential attacks and curated wordlists.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[CeWL](https://github.com/digininja/CeWL)** | ![Stars](https://img.shields.io/github/stars/digininja/CeWL?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/digininja/CeWL?style=flat&label=&color=555) | Spiders a website to build a custom, target-specific wordlist. |
| **[Hashcat](https://github.com/hashcat/hashcat)** | ![Stars](https://img.shields.io/github/stars/hashcat/hashcat?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/hashcat/hashcat?style=flat&label=&color=555) | The world's fastest password recovery tool, GPU-accelerated. |
| **[John the Ripper](https://github.com/openwall/john)** | ![Stars](https://img.shields.io/github/stars/openwall/john?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/openwall/john?style=flat&label=&color=555) | Veteran password cracker supporting hundreds of hash and cipher types. |
| **[SecLists](https://github.com/danielmiessler/SecLists)** | ![Stars](https://img.shields.io/github/stars/danielmiessler/SecLists?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/danielmiessler/SecLists?style=flat&label=&color=555) | The collection of wordlists — usernames, passwords, payloads and more. |
| **[THC-Hydra](https://github.com/vanhauser-thc/thc-hydra)** | ![Stars](https://img.shields.io/github/stars/vanhauser-thc/thc-hydra?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/vanhauser-thc/thc-hydra?style=flat&label=&color=555) | Fast network login brute-forcer supporting many protocols. |

[⬆ Back to top](#contents)

## Wireless & Network Attacks

*Wi-Fi auditing, man-in-the-middle and layer-2 attack tooling.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng)** | ![Stars](https://img.shields.io/github/stars/aircrack-ng/aircrack-ng?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/aircrack-ng/aircrack-ng?style=flat&label=&color=555) | Complete suite for auditing and cracking Wi-Fi (WEP/WPA) security. |
| **[bettercap](https://github.com/bettercap/bettercap)** | ![Stars](https://img.shields.io/github/stars/bettercap/bettercap?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/bettercap/bettercap?style=flat&label=&color=555) | Swiss-army knife for network attacks and monitoring (Wi-Fi, BLE, MITM). |
| **[Kismet](https://github.com/kismetwireless/kismet)** | ![Stars](https://img.shields.io/github/stars/kismetwireless/kismet?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/kismetwireless/kismet?style=flat&label=&color=555) | Wireless network and device detector, sniffer and IDS. |
| **[Wifiphisher](https://github.com/wifiphisher/wifiphisher)** | ![Stars](https://img.shields.io/github/stars/wifiphisher/wifiphisher?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/wifiphisher/wifiphisher?style=flat&label=&color=555) | Rogue access point framework for red-team Wi-Fi phishing assessments. |
| **[Wifite2](https://github.com/derv82/wifite2)** | ![Stars](https://img.shields.io/github/stars/derv82/wifite2?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/derv82/wifite2?style=flat&label=&color=555) | Automated wireless attack tool that orchestrates the aircrack-ng suite. |

[⬆ Back to top](#contents)

## Reverse Engineering

*Disassemblers, decompilers and debuggers for taking binaries apart.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Cutter](https://github.com/rizinorg/cutter)** | ![Stars](https://img.shields.io/github/stars/rizinorg/cutter?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/rizinorg/cutter?style=flat&label=&color=555) | Free and open-source GUI for reverse engineering, powered by Rizin. |
| **[Ghidra](https://github.com/NationalSecurityAgency/ghidra)** | ![Stars](https://img.shields.io/github/stars/NationalSecurityAgency/ghidra?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/NationalSecurityAgency/ghidra?style=flat&label=&color=555) | The NSA's open-source software reverse-engineering suite and decompiler. |
| **[radare2](https://github.com/radareorg/radare2)** | ![Stars](https://img.shields.io/github/stars/radareorg/radare2?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/radareorg/radare2?style=flat&label=&color=555) | Unix-like reverse-engineering framework and command-line toolset. |
| **[Rizin](https://github.com/rizinorg/rizin)** | ![Stars](https://img.shields.io/github/stars/rizinorg/rizin?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/rizinorg/rizin?style=flat&label=&color=555) | Reverse-engineering framework forked from radare2 with a focus on usability. |
| **[x64dbg](https://github.com/x64dbg/x64dbg)** | ![Stars](https://img.shields.io/github/stars/x64dbg/x64dbg?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/x64dbg/x64dbg?style=flat&label=&color=555) | Open-source x64/x32 debugger for Windows binaries. |

[⬆ Back to top](#contents)

## Malware Analysis

*Sandboxes, detection rules and tooling for studying malicious code.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[capa](https://github.com/mandiant/capa)** | ![Stars](https://img.shields.io/github/stars/mandiant/capa?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/mandiant/capa?style=flat&label=&color=555) | Identifies capabilities in executable files from their code. |
| **[CAPEv2](https://github.com/kevoreilly/CAPEv2)** | ![Stars](https://img.shields.io/github/stars/kevoreilly/CAPEv2?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/kevoreilly/CAPEv2?style=flat&label=&color=555) | Malware sandbox with automated config and payload extraction. |
| **[FLARE FLOSS](https://github.com/mandiant/flare-floss)** | ![Stars](https://img.shields.io/github/stars/mandiant/flare-floss?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/mandiant/flare-floss?style=flat&label=&color=555) | Automatically extracts obfuscated strings from malware. |
| **[pe-sieve](https://github.com/hasherezade/pe-sieve)** | ![Stars](https://img.shields.io/github/stars/hasherezade/pe-sieve?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/hasherezade/pe-sieve?style=flat&label=&color=555) | Scans running processes for in-memory code implants and hooks. |
| **[YARA](https://github.com/VirusTotal/yara)** | ![Stars](https://img.shields.io/github/stars/VirusTotal/yara?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/VirusTotal/yara?style=flat&label=&color=555) | The pattern-matching swiss knife for identifying and classifying malware. |

[⬆ Back to top](#contents)

## Digital Forensics & DFIR

*Memory, disk and endpoint forensics for incident response investigations.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Autopsy](https://github.com/sleuthkit/autopsy)** | ![Stars](https://img.shields.io/github/stars/sleuthkit/autopsy?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/sleuthkit/autopsy?style=flat&label=&color=555) | Graphical digital forensics platform built on The Sleuth Kit. |
| **[GRR Rapid Response](https://github.com/google/grr)** | ![Stars](https://img.shields.io/github/stars/google/grr?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/google/grr?style=flat&label=&color=555) | Incident response framework for remote live forensics across many hosts. |
| **[The Sleuth Kit](https://github.com/sleuthkit/sleuthkit)** | ![Stars](https://img.shields.io/github/stars/sleuthkit/sleuthkit?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/sleuthkit/sleuthkit?style=flat&label=&color=555) | Library and command-line tools for disk image and file-system forensics. |
| **[Velociraptor](https://github.com/Velocidex/velociraptor)** | ![Stars](https://img.shields.io/github/stars/Velocidex/velociraptor?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/Velocidex/velociraptor?style=flat&label=&color=555) | Endpoint visibility and digital forensics at scale with its own query language. |
| **[Volatility 3](https://github.com/volatilityfoundation/volatility3)** | ![Stars](https://img.shields.io/github/stars/volatilityfoundation/volatility3?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/volatilityfoundation/volatility3?style=flat&label=&color=555) | The advanced memory forensics framework for analysing RAM captures. |

[⬆ Back to top](#contents)

## Threat Intelligence

*Platforms for collecting, correlating and sharing threat intelligence.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[MISP](https://github.com/MISP/MISP)** | ![Stars](https://img.shields.io/github/stars/MISP/MISP?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/MISP/MISP?style=flat&label=&color=555) | Open-source threat intelligence and sharing platform for IoCs. |
| **[MISP Warninglists](https://github.com/MISP/misp-warninglists)** | ![Stars](https://img.shields.io/github/stars/MISP/misp-warninglists?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/MISP/misp-warninglists?style=flat&label=&color=555) | Lists to warn against false positives in indicators of compromise. |
| **[OpenCTI](https://github.com/OpenCTI-Platform/opencti)** | ![Stars](https://img.shields.io/github/stars/OpenCTI-Platform/opencti?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/OpenCTI-Platform/opencti?style=flat&label=&color=555) | Platform for structuring, storing and visualising cyber threat intelligence. |
| **[TheHive](https://github.com/TheHive-Project/TheHive)** | ![Stars](https://img.shields.io/github/stars/TheHive-Project/TheHive?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/TheHive-Project/TheHive?style=flat&label=&color=555) | Scalable, collaborative security incident response platform. |
| **[Yeti](https://github.com/yeti-platform/yeti)** | ![Stars](https://img.shields.io/github/stars/yeti-platform/yeti?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/yeti-platform/yeti?style=flat&label=&color=555) | Your everyday threat intelligence — repository of observables and TTPs. |

[⬆ Back to top](#contents)

## Detection & Blue Team

*Detection rules, IDS/IPS and monitoring for defenders.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Security Onion](https://github.com/Security-Onion-Solutions/securityonion)** | ![Stars](https://img.shields.io/github/stars/Security-Onion-Solutions/securityonion?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/Security-Onion-Solutions/securityonion?style=flat&label=&color=555) | Linux distro for threat hunting, network monitoring and log management. |
| **[Sigma](https://github.com/SigmaHQ/sigma)** | ![Stars](https://img.shields.io/github/stars/SigmaHQ/sigma?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/SigmaHQ/sigma?style=flat&label=&color=555) | Generic, shareable detection rules for SIEMs — the 'YARA for logs'. |
| **[Suricata](https://github.com/OISF/suricata)** | ![Stars](https://img.shields.io/github/stars/OISF/suricata?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/OISF/suricata?style=flat&label=&color=555) | High-performance network IDS, IPS and network security monitoring engine. |
| **[Wazuh](https://github.com/wazuh/wazuh)** | ![Stars](https://img.shields.io/github/stars/wazuh/wazuh?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/wazuh/wazuh?style=flat&label=&color=555) | Open-source XDR/SIEM: host intrusion detection, log analysis and response. |
| **[Zeek](https://github.com/zeek/zeek)** | ![Stars](https://img.shields.io/github/stars/zeek/zeek?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/zeek/zeek?style=flat&label=&color=555) | Powerful network analysis framework focused on security monitoring. |

[⬆ Back to top](#contents)

## Hardening & Defense

*Harden hosts, servers and configurations to shrink the attack surface before an attack.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[koncreet](https://github.com/jimididit/koncreet)** | ![Stars](https://img.shields.io/github/stars/jimididit/koncreet?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/jimididit/koncreet?style=flat&label=&color=555) | First-hour hardening toolkit for a new Linux VPS. |
| **[Lynis](https://github.com/CISOfy/lynis)** | ![Stars](https://img.shields.io/github/stars/CISOfy/lynis?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/CISOfy/lynis?style=flat&label=&color=555) | Security auditing and hardening tool for Unix/Linux systems. |
| **[OpenSCAP](https://github.com/OpenSCAP/openscap)** | ![Stars](https://img.shields.io/github/stars/OpenSCAP/openscap?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/OpenSCAP/openscap?style=flat&label=&color=555) | Scans systems against SCAP security baselines and hardening policies. |
| **[ssh-audit](https://github.com/jtesta/ssh-audit)** | ![Stars](https://img.shields.io/github/stars/jtesta/ssh-audit?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/jtesta/ssh-audit?style=flat&label=&color=555) | Audits SSH server and client configuration for weak settings. |

[⬆ Back to top](#contents)

## Cloud & Container Security

*Auditing and attacking cloud accounts, Kubernetes and container images.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[kube-hunter](https://github.com/aquasecurity/kube-hunter)** | ![Stars](https://img.shields.io/github/stars/aquasecurity/kube-hunter?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/aquasecurity/kube-hunter?style=flat&label=&color=555) | Hunts for security weaknesses in Kubernetes clusters. |
| **[Pacu](https://github.com/RhinoSecurityLabs/pacu)** | ![Stars](https://img.shields.io/github/stars/RhinoSecurityLabs/pacu?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/RhinoSecurityLabs/pacu?style=flat&label=&color=555) | AWS exploitation framework for testing cloud environment security. |
| **[Prowler](https://github.com/prowler-cloud/prowler)** | ![Stars](https://img.shields.io/github/stars/prowler-cloud/prowler?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/prowler-cloud/prowler?style=flat&label=&color=555) | Security assessment and hardening for AWS, Azure, GCP and Kubernetes. |
| **[ScoutSuite](https://github.com/nccgroup/ScoutSuite)** | ![Stars](https://img.shields.io/github/stars/nccgroup/ScoutSuite?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/nccgroup/ScoutSuite?style=flat&label=&color=555) | Multi-cloud security auditing tool for AWS, Azure, GCP and more. |
| **[Trivy](https://github.com/aquasecurity/trivy)** | ![Stars](https://img.shields.io/github/stars/aquasecurity/trivy?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/aquasecurity/trivy?style=flat&label=&color=555) | All-in-one scanner for containers, IaC, code and cloud misconfigurations. |

[⬆ Back to top](#contents)

## Mobile Security

*Static and dynamic analysis for Android and iOS applications.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Apktool](https://github.com/iBotPeaches/Apktool)** | ![Stars](https://img.shields.io/github/stars/iBotPeaches/Apktool?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/iBotPeaches/Apktool?style=flat&label=&color=555) | Reverse-engineers Android APKs: decode resources and rebuild them. |
| **[Frida](https://github.com/frida/frida)** | ![Stars](https://img.shields.io/github/stars/frida/frida?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/frida/frida?style=flat&label=&color=555) | Dynamic instrumentation toolkit for hooking apps at runtime. |
| **[jadx](https://github.com/skylot/jadx)** | ![Stars](https://img.shields.io/github/stars/skylot/jadx?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/skylot/jadx?style=flat&label=&color=555) | Dex to Java decompiler with a handy GUI for inspecting Android apps. |
| **[MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)** | ![Stars](https://img.shields.io/github/stars/MobSF/Mobile-Security-Framework-MobSF?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/MobSF/Mobile-Security-Framework-MobSF?style=flat&label=&color=555) | Automated static and dynamic analysis for Android and iOS apps. |
| **[objection](https://github.com/sensepost/objection)** | ![Stars](https://img.shields.io/github/stars/sensepost/objection?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/sensepost/objection?style=flat&label=&color=555) | Runtime mobile exploration powered by Frida — no jailbreak/root needed. |

[⬆ Back to top](#contents)

## Vulnerability Scanning

*Scanners that find known vulnerabilities and misconfigurations.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[Grype](https://github.com/anchore/grype)** | ![Stars](https://img.shields.io/github/stars/anchore/grype?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/anchore/grype?style=flat&label=&color=555) | Vulnerability scanner for container images and filesystems. |
| **[Nuclei](https://github.com/projectdiscovery/nuclei)** | ![Stars](https://img.shields.io/github/stars/projectdiscovery/nuclei?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/projectdiscovery/nuclei?style=flat&label=&color=555) | Template-based scanner for known CVEs and misconfigurations at scale. |
| **[OpenVAS / Greenbone](https://github.com/greenbone/openvas-scanner)** | ![Stars](https://img.shields.io/github/stars/greenbone/openvas-scanner?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/greenbone/openvas-scanner?style=flat&label=&color=555) | Full-featured open-source vulnerability scanner and management stack. |
| **[OSV-Scanner](https://github.com/google/osv-scanner)** | ![Stars](https://img.shields.io/github/stars/google/osv-scanner?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/google/osv-scanner?style=flat&label=&color=555) | Scans project dependencies for known vulnerabilities using the OSV database. |
| **[Wapiti](https://github.com/wapiti-scanner/wapiti)** | ![Stars](https://img.shields.io/github/stars/wapiti-scanner/wapiti?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/wapiti-scanner/wapiti?style=flat&label=&color=555) | Black-box web vulnerability scanner that audits app security. |

[⬆ Back to top](#contents)

## CTF & Training

*Platforms, vulnerable targets and cheat sheets for learning offensive security.*

| Tool | Stars | Last commit | Description |
| --- | --- | --- | --- |
| **[CTFd](https://github.com/CTFd/CTFd)** | ![Stars](https://img.shields.io/github/stars/CTFd/CTFd?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/CTFd/CTFd?style=flat&label=&color=555) | The easy-to-use, customisable capture-the-flag framework. |
| **[HackTricks](https://github.com/HackTricks-wiki/hacktricks)** | ![Stars](https://img.shields.io/github/stars/HackTricks-wiki/hacktricks?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/HackTricks-wiki/hacktricks?style=flat&label=&color=555) | Encyclopaedic collection of pentesting tricks and techniques. |
| **[Metasploitable3](https://github.com/rapid7/metasploitable3)** | ![Stars](https://img.shields.io/github/stars/rapid7/metasploitable3?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/rapid7/metasploitable3?style=flat&label=&color=555) | Intentionally vulnerable VM for practising exploitation. |
| **[OWASP Juice Shop](https://github.com/juice-shop/juice-shop)** | ![Stars](https://img.shields.io/github/stars/juice-shop/juice-shop?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/juice-shop/juice-shop?style=flat&label=&color=555) | Deliberately insecure web app for training and CTFs. |
| **[OWASP WebGoat](https://github.com/WebGoat/WebGoat)** | ![Stars](https://img.shields.io/github/stars/WebGoat/WebGoat?style=flat&label=&color=444) | ![Last commit](https://img.shields.io/github/last-commit/WebGoat/WebGoat?style=flat&label=&color=555) | Deliberately insecure Java app teaching web security lessons. |

[⬆ Back to top](#contents)

---

## Contributing

This list is generated from the TOML files in [`data/`](data/). Do **not** edit `README.md` by hand — edit the data and run `python3 generate.py`. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.

