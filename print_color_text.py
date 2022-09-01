import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.WHITE +"This is a console text color.")
print(Back.MAGENTA+"This is a console text color.")
print(Fore.GREEN+Style.DIM +"This is a console text color.")
print(Fore.RED +"This is a console text color.")

# san ="san"

# d = f"""
# {san} deep
# """

# print(d)