import os
import sys
import subprocess
import time

try:
    import requests
except ModuleNotFoundError:
    print("\033[91m[!] 'requests' module not found. Installing...\033[0m")
    os.system("pip install requests")
    import requests

def clear_screen():
    os.system('clear')

def banner():
    # Menggunakan warna hijau matrix terang (\033[1;32m atau \033[92m dengan bold)
    print(r"""
\033[1;32m
 _  _ ____ ____  _  _  _  _ 
 |\ | |___ |  |  |__|  |  | 
 | \| |___ |__|     |  |__| 
                            
\033[0m\033[96m   Neo4script - Silent. Stealth. Secure.\033[0m
""")
    print("--------------------------------------------------")

def menu_update():
    print("\n\033[93m[+] Running System Update & Upgrade...\033[0m")
    os.system("pkg update && pkg upgrade -y")
    input("\nPress Enter to return to the menu...")

def menu_whoame():
    print("\n\033[93m[+] User & Network Information:\033[0m")
    try:
        username = subprocess.check_output("whoami", shell=True).decode().strip()
        print(f" * Termux Username : {username}")
        
        response = requests.get("https://ipinfo.io/json", timeout=5)
        data = response.json()
        
        ip = data.get("ip", "Unknown")
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        org = data.get("org", "Unknown")
        
        print(f" * Public IP       : {ip}")
        print(f" * Location        : {city}, {region}, {country}")
        print(f" * ISP / Network   : {org}")
    except Exception as e:
        print(f" [-] Failed to get network info: {e}")
    
    input("\nPress Enter to return to the menu...")

def menu_hacking_tools():
    print("\n\033[93m[+] Hacking Tools Installation (Nmap, John the Ripper, SQLMap, etc.)...\033[0m")
    print("Installing base packages & security tools...")
    os.system("pkg install git python python-pip nmap john sqlmap -y")
    print("\n[+] Tools installation completed!")
    input("\nPress Enter to return to the menu...")

def menu_otp_engine():
    print("\n\033[93m[+] Launching OTP Engine Module...\033[0m")
    if os.path.exists("otp-main/main.py"):
        current_dir = os.getcwd()
        os.chdir("otp-main")
        try:
            os.system("python main.py")
        finally:
            os.chdir(current_dir)
    else:
        print(" [-] Directory 'otp-main' or 'main.py' not found. Please make sure the zip is extracted correctly.")
    input("\nPress Enter to return to the menu...")

def main():
    while True:
        clear_screen()
        banner()
        print("Select menu:")
        print("1. Update & Upgrade")
        print("2. WhoaMe")
        print("3. Install Hacking Tools")
        print("4. OTP Engine")
        print("5. Exit")
        print("--------------------------------------------------")
        
        pilihan = input("Enter
