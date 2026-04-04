# 🔍 Zudio Recon Framework

> A multi-threaded offensive reconnaissance framework built in Python.
> For educational and authorized security testing only.

---

## ⚡ Features

- 🔎 Automatic tool checker — detects missing tools
- 📦 Auto installer — installs missing tools with user permission
- 🧵 Multi-threaded — runs all tools simultaneously
- 🌐 Smart URL parsing — handles any input format
- 📄 Clean report generation with timestamp
- 🔁 Run multiple targets in one session

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| `nmap` | Port scanning |
| `whois` | Domain registration info |
| `dig` | DNS records |
| `curl` | HTTP headers |
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
```
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

This tool is for **educational purposes** and **authorized penetration testing only**.
Do not use against systems you do not have explicit permission to test.
The developer is not responsible for any misuse.

---

## 👨‍💻 Author

**zudio-infosec** — Cybersecurity Student | Offensive Security Learner
