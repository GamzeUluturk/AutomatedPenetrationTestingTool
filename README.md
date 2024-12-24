# AutomatedPenetrationTestingTool

Exploit Toolkit for Metasploitable 2

This repository contains Python-based exploits and a collection of ready-to-use tools designed to test and exploit known vulnerabilities in the Metasploitable 2 virtual machine. It provides an all-in-one toolkit for ethical hackers and security researchers to practice and develop their skills.


![Screenshot 2024-12-24 002757](https://github.com/user-attachments/assets/ef1a9c48-a3f2-4ed6-8e33-51b9fabe4186)

![Screenshot 2024-12-24 010143](https://github.com/user-attachments/assets/08d7bb40-8d61-479e-8783-403e2338b706)

![Screenshot 2024-12-24 010301](https://github.com/user-attachments/assets/43a14c8e-1deb-4369-a6d3-9fe7197443cf)

Exploits:

- SSH Brute Force Attack (ssh_exploit.py)
  
  Performs brute-force attacks on SSH services to test weak credentials.

- FTP Anonymous Access Exploit (ftp_exploit.py)
  
  Checks and exploits anonymous access vulnerabilities in FTP services.

- SMB Exploit (smb_exploit.py)

  Retrieves user information and files from vulnerable SMB services.

- VNC Authentication Bypass (vnc_exploit.py)

  Tests for authentication bypass vulnerabilities in VNC services.

- DistCC Remote Code Execution (distcc_exploit.py)

  Executes remote commands using the DistCC service vulnerability.

- Ingreslock Exploit (ingreslock_exploit.py)

  Exploits the ingreslock backdoor to establish connections.

- UnrealIRCd Remote Code Execution (unreal_exploit.py)

  Targets UnrealIRCd vulnerabilities to execute remote code.

Built-in Tools:

In addition to the custom exploits, the toolkit includes ready-to-use tools for scanning, enumeration, and exploitation:

- Nmap Scan - Network scanning and host discovery.
- Feroxbuster Scan - Fast and efficient directory brute-forcing.
- Gobuster Scan - Directory and DNS brute-forcing.
- Nikto Scan - Web server vulnerability scanning.
- Hydra Brute Force - Brute-force password cracking.
- Metasploit Console - Comprehensive framework for exploitation and post-exploitation.

These tools can be launched directly from the Exploit and Tool Menu.
  
