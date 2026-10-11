# 🔍 Zudio Recon Framework

> A multi-threaded offensive reconnaissance framework built in Python for authorized security testing.

---

## ⚡ Features

- 🔎 **Automatic tool checker** — detects missing tools on startup
- 📦 **Auto installer** — installs missing tools with user permission
- 🧵 **Multi-threaded execution** — runs all reconnaissance tools simultaneously for speed
- 🌐 **Smart URL parsing** — handles various input formats seamlessly
- 📄 **Clean report generation** — creates timestamped, structured reports
- 🔁 **Bulk targets** — run multiple targets in a single session

---

## 🛠️ Tools Integrated

| Tool | Purpose |
|---|---|
| `nmap` | Port scanning & service detection |
| `whois` | Domain registration & ownership info |
| `dig` | DNS record lookup |
| `curl` | HTTP header analysis |
| `amass` | Subdomain enumeration |
| `nikto` | Web vulnerability scanning |

---

## 🚀 Usage

```bash
git clone https://github.com/zudio-infosec/zudio-recon-framework.git
cd zudio-recon-framework
pip install colorama
python3 recon.py
```

---

## 📄 Sample Report Output

```text
============================================================
  ZUDIO RECON FRAMEWORK — REPORT
  Target    : example.com
  Generated : 2026-04-04_23-23-22
============================================================

[ NMAP ]
PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https

[ WHOIS ]
Registrar: Example Registrar
Creation Date: 2010-01-01

[ DIG ]
example.com. IN A 93.184.216.34
============================================================
```

---

## ⚠️ Disclaimer

This tool is strictly for **educational purposes** and **authorized penetration testing only**. 

**Do not use this tool against systems you do not have explicit, written permission to test.** The developer is not responsible for any misuse or illegal activity.

---

## 👨‍💻 Author

**Hasham Javed (Zudio)** — Cybersecurity Student | Offensive Security Learner
[Portfolio](https://zudio-infosec.github.io/) | [LinkedIn](https://www.linkedin.com/in/hasham-javed-a03424400/)
