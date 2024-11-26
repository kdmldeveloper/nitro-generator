import random
import string
import requests
import os
import sys
import time
import platform
from colorama import Fore, init
import subprocess

init(autoreset=True)

class NitroGen:
    def __init__(self):
        self.start_time = time.strftime("%H:%M:%S")
        self.computer_name = platform.node()

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_license(self):
        license_text = f"""
{Fore.CYAN}### Kullanım Lisansı ###
{Fore.YELLOW}1. Bu kodu kullanabilirsiniz, öğrenebilirsiniz ve kendi projelerinizde kullanabilirsiniz.
2. Kodu {Fore.RED}değiştirerek paylaşamaz{Fore.YELLOW} veya {Fore.RED}satamazsınız{Fore.YELLOW}.
3. Kodun bu lisans şartlarına uygun olarak kullanılması gereklidir.
{Fore.LIGHTBLUE_EX}Yazar: ErayDev | GitHub: https://github.com/kdmldeveloper
{Fore.CYAN}----------------------------------------------
        """
        print(license_text)
        time.sleep(3)

    def quickChecker(self, nitro: str):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.GREEN + f"Valid | {nitro}")
            return True
        else:
            print(Fore.RED + f"Invalid | {nitro}")
            return False

    def run(self):
        print(Fore.YELLOW + "Nitro Kodları Üretme ve Kontrol Etme Başladı...\n")
        valid = []
        invalid = 0
        chars = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(chars, k=16))
            url = f"https://discord.gift/{code}"
            result = self.quickChecker(url)
            if result:
                valid.append(url)
                input(Fore.GREEN + "Geçerli bir kod bulundu! Devam etmek için herhangi bir tuşa basın...")
            else:
                invalid += 1

    def start(self):
        self.clear_terminal()
        self.show_license()
        print(Fore.CYAN + f"Çalışan Bilgisayar: {self.computer_name}")
        print(Fore.CYAN + f"Saat: {self.start_time}")
        print(Fore.MAGENTA + "Yapımcı: ErayDev")
        print(Fore.MAGENTA + "GitHub: https://github.com/kdmldeveloper\n")
        choice = input(Fore.YELLOW + "Üretmeye başlamak istiyor musunuz? (evet/hayır): ").strip().lower()
        if choice == "evet":
            self.clear_terminal()
            print(Fore.CYAN + f"Çalışan Bilgisayar: {self.computer_name}")
            print(Fore.CYAN + f"Saat: {self.start_time}")
            print(Fore.MAGENTA + "Yapımcı: ErayDev")
            print(Fore.MAGENTA + "GitHub: https://github.com/kdmldeveloper\n")
            self.run()
        elif choice == "hayır":
            print(Fore.RED + "Programdan çıkılıyor...")
            sys.exit()
        else:
            print(Fore.RED + "Geçersiz seçim. Programdan çıkılıyor...")
            sys.exit()

if __name__ == '__main__':
    gen = NitroGen()
    gen.start()
