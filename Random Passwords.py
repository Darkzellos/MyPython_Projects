import random
from colorama import Fore, Back, Style, init
import pyperclip
init(convert=True)
letters = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1' '2' '3' '4' '5' '6' '7' '8' '9' '10']
print(Fore.GREEN + "----------PASSWORD-------------" + Style.RESET_ALL)	
num = 0
while num < 10:
	num = num + 1
	password = print(Fore.RED + random.choice(letters) + Style.RESET_ALL, end='')
again = input("\nЧтобы продолжить нажмите Enter")