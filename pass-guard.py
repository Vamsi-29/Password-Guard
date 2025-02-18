import re
import sys
import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init()

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Criteria for password strength
    if len(password) < 8:
        suggestions.append("Make your password at least 8 characters long.")
    else:
        strength += 1

    if not re.search(r"[A-Z]", password):
        suggestions.append("Add at least one uppercase letter.")
    else:
        strength += 1

    if not re.search(r"[a-z]", password):
        suggestions.append("Add at least one lowercase letter.")
    else:
        strength += 1

    if not re.search(r"[0-9]", password):
        suggestions.append("Include at least one number.")
    else:
        strength += 1

    if not re.search(r"[@$!%*?&#^+=-_]", password):
        suggestions.append("Use at least one special character (e.g., @, #, !, &).")
    else:
        strength += 1

    return strength, suggestions

def generate_strong_password(password):
    missing_chars = []
    if not re.search(r"[A-Z]", password):
        missing_chars.append(random.choice(string.ascii_uppercase))
    if not re.search(r"[a-z]", password):
        missing_chars.append(random.choice(string.ascii_lowercase))
    if not re.search(r"[0-9]", password):
        missing_chars.append(random.choice(string.digits))
    if not re.search(r"[@$!%*?&#^+=-_]", password):
        missing_chars.append(random.choice("@$!%*?&#^+=-_") )

    new_password = list(password) + missing_chars
    while len(new_password) < 12:
        new_password.append(random.choice(string.ascii_letters + string.digits + "@$!%*?&#^+=-_") )

    random.shuffle(new_password)
    return "".join(new_password)

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
    strength, suggestions = check_password_strength(password)

    if strength <= 2:
        print(Fore.RED + "[Weak] Your password is too weak!" + Style.RESET_ALL)
    elif strength == 3 or strength == 4:
        print(Fore.YELLOW + "[Medium] Your password is fairly strong." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "[Strong] Your password is very strong!" + Style.RESET_ALL)

    if suggestions:
        print(Fore.CYAN + "\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print("- " + suggestion)
        print(Style.RESET_ALL)

        strong_password = generate_strong_password(password)
        print(Fore.MAGENTA + "\nSuggested Strong Password: " + strong_password + Style.RESET_ALL)

if __name__ == "__main__":
    main()
