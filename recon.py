# # recon.py Zudio-recon Framework

# import threading
# import subprocess
# import os
# from colorama import Fore, Style, init
# from urllib.parse import urlparse

# init(autoreset=True)

# RED = Fore.RED
# GREEN = Fore.GREEN
# YELLOW = Fore.YELLOW
# CYAN = Fore.CYAN
# BOLD = Style.BRIGHT
# RESET = Style.RESET_ALL

# def banner():
#     print (CYAN + BOLD + """
           
#            ╔═════════════════════════════════╗
#            ║                                 ║
#            ║     ZUDIO-Recon  Framework      ║ 
#            ║       Offensive Security        ║
#            ║                                 ║
#            ╚═════════════════════════════════╝
#            """)

# TOOLS = {
#     "nmap": "apt install nmap -y",
#     "whois": "apt install whois -y",
#     "amass": "apt install amass -y",
#     "dig": "apt install dnsutils -y",
#     "curl": "apt install curl -y",
#     "nikto": "apt install nikto -y"
# }

# results = {}

# def check_tools():
#     print(YELLOW + "\n[*] Checking required tools...\n")
#     missing = []

#     for tool in TOOLS:
#         result = subprocess.run(
#             ["which", tool],
#             capture_output=True,
#             text=True
#         )
#         if result.returncode == 0:
#             print(GREEN + f"    [+] {tool:<12} ✓ installed")
#         else:
#             print(RED + f"    [-] {tool:<12} ✗ missing")
#             missing.append(tool)

#     return missing


# def install_tools(missing):
#     print(YELLOW + "\n[!] Missing tools found\n")

#     for tool in missing:
#         command = TOOLS[tool]
#         print(CYAN + f"    [?] Install {tool}?")
#         print(CYAN + f"    [>] Command: {command}")
#         print(YELLOW + "    [?] Proceed? (y/n): ", end="")
#         choice = input().strip().lower()

#         if choice == "y":
#             print(YELLOW + f"    [*] Installing {tool}...", end=" ")
#             subprocess.run(
#                 command,
#                 shell=True,
#                 stdout=subprocess.DEVNULL,
#                 stderr=subprocess.DEVNULL
#             )
#             print(GREEN + "✓ Done!")
#         else:
#             print(RED + f"    [-] Skipping {tool}")


# def get_target():
#     while True:
#         target = input(YELLOW + "\n[?] Enter target domain: ")
        
#         if target == "":
#             print(RED + "[!] Cannot be empty. Try again.")
#         else:
#             parsed = urlparse(target)
#             if parsed.netloc:
#                 target = parsed.netloc
#             print(GREEN + f"[+] Target set: {target}")
#             return target
        

# def run_recon(target):
#     print(CYAN + f"\n[*] Starting recon on {target}...\n")
    
#     threads = []
    
#     for tool in TOOLS:
#         t = threading.Thread(target=run_tool, args=(tool, target))
#         threads.append(t)
#         t.start()
    
#     for t in threads:
#         t.join()
    
#     print(GREEN + "\n[+] All tools finished!\n")


# def run_tool(tool, target):
#     print(YELLOW + f"    [*] Running {tool}...")
    
#     commands = {
#         "nmap": f"nmap -sV --open {target}",
#         "whois": f"whois {target}",
#         "dig": f"dig {target}",
#         "curl": f"curl -I {target}",
#         "amass": f"amass enum -d {target}",
#         "nikto": f"nikto -h {target}"
#     }
    
#     command = commands[tool]
    
#     try:
#         result = subprocess.run(
#             command,
#             shell=True,
#             capture_output=True,
#             text=True,
#             timeout=60
#         )
#         results[tool] = result.stdout
#         print(GREEN + f"    [+] {tool} done!")
#     except subprocess.TimeoutExpired:
#         results[tool] = f"{tool} timed out after 60 seconds"
#         print(YELLOW + f"    [!] {tool} timed out!")


# try:
#     banner()
#     missing = check_tools()
#     if missing:
#         install_tools(missing)
#     target = get_target()
#     run_recon(target)
# except KeyboardInterrupt:
#     print(RED + "\n\n[!] Interrupted. Exiting...\n")


# recon.py Zudio-recon Framework

import threading
import subprocess
import os
from colorama import Fore, Style, init
from urllib.parse import urlparse
from datetime import datetime

init(autoreset=True)

RED    = Fore.RED
GREEN  = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN   = Fore.CYAN
BOLD   = Style.BRIGHT
RESET  = Style.RESET_ALL

TOOLS = {
    "nmap"  : "apt install nmap -y",
    "whois" : "apt install whois -y",
    "amass" : "apt install amass -y",
    "dig"   : "apt install dnsutils -y",
    "curl"  : "apt install curl -y",
    "nikto" : "apt install nikto -y"
}

TIMEOUTS = {
    "nmap"  : 120,
    "whois" : 30,
    "dig"   : 30,
    "curl"  : 30,
    "amass" : 300,
    "nikto" : 300
}

results = {}

def banner():
    print(CYAN + BOLD + """
╔═════════════════════════════════╗
║                                 ║
║     ZUDIO-Recon  Framework      ║
║       Offensive Security        ║
║                                 ║
╚═════════════════════════════════╝
    """)

def check_tools():
    print(YELLOW + "\n[*] Checking required tools...\n")
    missing = []
    for tool in TOOLS:
        result = subprocess.run(
            ["which", tool],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(GREEN + f"    [+] {tool:<12} ✓ installed")
        else:
            print(RED + f"    [-] {tool:<12} ✗ missing")
            missing.append(tool)
    return missing

def install_tools(missing):
    print(YELLOW + "\n[!] Missing tools found\n")
    for tool in missing:
        command = TOOLS[tool]
        print(CYAN  + f"    [?] Install {tool}?")
        print(CYAN  + f"    [>] Command: {command}")
        print(YELLOW + "    [?] Proceed? (y/n): ", end="")
        choice = input().strip().lower()
        if choice == "y":
            print(YELLOW + f"    [*] Installing {tool}...", end=" ")
            subprocess.run(
                command,
                shell=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(GREEN + "✓ Done!")
        else:
            print(RED + f"    [-] Skipping {tool}")

def get_target():
    while True:
        target = input(YELLOW + "\n[?] Enter target domain: ")
        if target == "":
            print(RED + "[!] Cannot be empty. Try again.")
        else:
            parsed = urlparse(target)
            if parsed.netloc:
                target = parsed.netloc
            print(GREEN + f"[+] Target set: {target}")
            return target

def run_tool(tool, target):
    print(YELLOW + f"    [*] Running {tool}...")
    commands = {
        "nmap"  : f"nmap -F {target}",
        "whois" : f"whois {target}",
        "dig"   : f"dig {target}",
        "curl"  : f"curl -I {target}",
        "amass" : f"amass enum -d {target}",
        "nikto" : f"nikto -h {target}"
    }
    command = commands[tool]
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=TIMEOUTS[tool]
        )
        results[tool] = result.stdout
        print(GREEN + f"    [+] {tool} done!")
    except subprocess.TimeoutExpired:
        results[tool] = f"{tool} timed out after {TIMEOUTS[tool]} seconds"
        print(YELLOW + f"    [!] {tool} timed out!")

def run_recon(target):
    print(CYAN + f"\n[*] Starting recon on {target}...\n")
    threads = []
    for tool in TOOLS:
        t = threading.Thread(target=run_tool, args=(tool, target))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(GREEN + "\n[+] All tools finished!\n")

def generate_report(target):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename  = f"recon_{target}_{timestamp}.txt"

    print(CYAN + f"[*] Generating report → {filename}\n")

    with open(filename, "w") as f:
        f.write("=" * 60 + "\n")
        f.write(f"  ZUDIO RECON FRAMEWORK — REPORT\n")
        f.write(f"  Target    : {target}\n")
        f.write(f"  Generated : {timestamp}\n")
        f.write("=" * 60 + "\n\n")

        for tool, output in results.items():
            f.write(f"\n{'─' * 60}\n")
            f.write(f"  [ {tool.upper()} ]\n")
            f.write(f"{'─' * 60}\n")
            f.write(output if output else "No output captured.\n")
            f.write("\n")

        f.write("=" * 60 + "\n")
        f.write("  END OF REPORT\n")
        f.write("=" * 60 + "\n")

    print(GREEN + f"[+] Report saved → {filename}")
    return filename

def ask_run_again():
    print(YELLOW + "\n[?] Run recon on another target? (y/n): ", end="")
    choice = input().strip().lower()
    return choice == "y"

try:
    while True:
        banner()
        missing = check_tools()
        if missing:
            install_tools(missing)
        target = get_target()
        run_recon(target)
        generate_report(target)
        if not ask_run_again():
            print(CYAN + "\n[*] Goodbye!\n")
            break
except KeyboardInterrupt:
    print(RED + "\n\n[!] Interrupted. Exiting...\n")