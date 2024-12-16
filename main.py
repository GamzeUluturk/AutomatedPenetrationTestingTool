import subprocess
import os
from colorama import Fore, Style, init

# Initialize terminal colors
init(autoreset=True)

# Exploit and tool list
exploits = {
    "Ingreslock": "ingreslock_exploit.py",
    "SSH Brute Force": "ssh_exploit.py",
    "SMB Exploit": "smb_exploit.py",
    "VNC Brute Force": "vnc_exploit.py",
    "FTP Exploit": "ftp_exploit.py",
    "Distcc Exploit": "distcc_exploit.py",
    "Unreal IRCD Exploit": "unreal_exploit.py",
}

tools = [
    "Nmap Scan",
    "Feroxbuster Scan",
    "Gobuster Scan",
    "Nikto Scan",
    "Hydra Brute Force",
    "Metasploit Console"
]

def print_divider():
    """Creates a divider line."""
    print(f"{Fore.MAGENTA}\n{'-' * 50}{Style.RESET_ALL}")

def list_exploits():
    print(f"\n{Fore.BLUE}[+] Exploits:{Style.RESET_ALL}")
    for i, exploit in enumerate(exploits, 1):
        print(f"{Fore.YELLOW}{i}. {exploit}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{len(exploits) + 1}. Return to Main Menu{Style.RESET_ALL}")

def list_tools():
    print(f"\n{Fore.BLUE}[+] Available Tools:{Style.RESET_ALL}")
    for i, tool in enumerate(tools, 1):
        print(f"{Fore.YELLOW}{i}. {tool}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{len(tools) + 1}. Return to Main Menu{Style.RESET_ALL}")

def run_exploit(exploit_name):
    if exploit_name in exploits:
        script_path = exploits[exploit_name]
        print_divider()
        print(f"{Fore.GREEN}[+] Running {exploit_name} exploit...{Style.RESET_ALL}")
        print_divider()
        os.system(f"python3 {script_path}")
        print_divider()
        print(f"{Fore.GREEN}[+] {exploit_name} process completed!{Style.RESET_ALL}")
        print_divider()
    else:
        print(f"{Fore.RED}[-] Invalid selection!{Style.RESET_ALL}")

def run_tool(tool_name):
    print_divider()
    print(f"{Fore.GREEN}[+] Running {tool_name} tool...{Style.RESET_ALL}")
    print_divider()

    if tool_name == "Nmap Scan":
        target = input(f"{Fore.CYAN}Target IP or network (e.g., 192.168.1.0/24): {Style.RESET_ALL}")
        os.system(f"nmap -p- {target}")
    elif tool_name == "Feroxbuster Scan":
        url = input(f"{Fore.CYAN}Target URL (e.g., http://192.168.1.1): {Style.RESET_ALL}")
        os.system(f"feroxbuster -u {url}")
    elif tool_name == "Gobuster Scan":
        url = input(f"{Fore.CYAN}Target URL (e.g., http://192.168.1.1): {Style.RESET_ALL}")
        wordlist = input(f"{Fore.CYAN}Specify wordlist file (e.g., /usr/share/wordlists/dirb/common.txt): {Style.RESET_ALL}")
        os.system(f"gobuster dir -u {url} -w {wordlist}")
    elif tool_name == "Nikto Scan":
        url = input(f"{Fore.CYAN}Target URL (e.g., http://192.168.1.1): {Style.RESET_ALL}")
        os.system(f"nikto -h {url}")
    elif tool_name == "Hydra Brute Force":
        target = input(f"{Fore.CYAN}Target IP or URL (e.g., 192.168.1.1): {Style.RESET_ALL}")
        service = input(f"{Fore.CYAN}Target service (e.g., ssh, ftp): {Style.RESET_ALL}")
        userlist = input(f"{Fore.CYAN}User list file (e.g., /usr/share/wordlists/userlist.txt): {Style.RESET_ALL}")
        passlist = input(f"{Fore.CYAN}Password list file (e.g., /usr/share/wordlists/passwords.txt): {Style.RESET_ALL}")
        os.system(f"hydra -L {userlist} -P {passlist} {target} {service}")
    elif tool_name == "Metasploit Console":
        os.system("msfconsole")
    else:
        print(f"{Fore.RED}[-] Invalid selection!{Style.RESET_ALL}")

    print_divider()
    print(f"{Fore.GREEN}[+] {tool_name} process completed!{Style.RESET_ALL}")
    print_divider()

def main():
    while True:
        print(f"\n{Fore.MAGENTA}=== Exploit and Tool Menu ==={Style.RESET_ALL}\n")
        print(f"{Fore.CYAN}1. List and Run Exploits{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. List and Run Tools{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.YELLOW}Make your selection: {Style.RESET_ALL}")
        
        if choice == "1":
            while True:
                list_exploits()
                exploit_choice = int(input(f"{Fore.YELLOW}Select the exploit you want to run: {Style.RESET_ALL}"))
                if exploit_choice == len(exploits) + 1:
                    print(f"{Fore.GREEN}[+] Returning to the main menu...{Style.RESET_ALL}")
                    break
                exploit_name = list(exploits.keys())[exploit_choice - 1]
                run_exploit(exploit_name)
        elif choice == "2":
            while True:
                list_tools()
                tool_choice = int(input(f"{Fore.YELLOW}Select the tool you want to run: {Style.RESET_ALL}"))
                if tool_choice == len(tools) + 1:
                    print(f"{Fore.GREEN}[+] Returning to the main menu...{Style.RESET_ALL}")
                    break
                tool_name = tools[tool_choice - 1]
                run_tool(tool_name)
        elif choice == "3":
            print(f"{Fore.GREEN}[+] Exiting...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[-] Invalid selection!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
