import re
import sys
from colorama import Fore, Style, init

# Initialize colorama
init()

def check_password_strength(password):
    strength = 0
    
    # Criteria for password strength
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[@$!%*?&#^+=-_]", password):
        strength += 1
    
    return strength

def main():
    print(Fore.CYAN + r"""
                ____              _  ____                     _
               |  _ \__      ____| |/ ___|_   _  __ _ _ __ __| |
               | |_) \ \ /\ / / _` | |  _| | | |/ _` | '__/ _` |
               |  __/ \ V  V / (_| | |_| | |_| | (_| | | | (_| |
               |_|     \_/\_/ \__,_|\____|\__,_|\__,_|_|  \__,_|
    
    """ + Style.RESET_ALL)
    print("Author: Vamsi Krishna")
    print("GitHub: https://github.com/VK-CyberSec\n")
    
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    
    if strength <= 2:
        print(Fore.RED + "[Weak] Your password is too weak!" + Style.RESET_ALL)
    elif strength == 3 or strength == 4:
        print(Fore.YELLOW + "[Medium] Your password is fairly strong." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "[Strong] Your password is very strong!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
