import platform
import sys
from sys import version_info

if version_info < (3, 0, 0):
    print('[!] Please use Python 3. $ python3 CyberPhish.py')
    sys.exit()

from Core.eletter import Instagram
from Core.eletter import Facebook
from Core.eletter import Gmail
from Core.eletter import Twitter
from Core.eletter import AskFM
from Core.eletter import Webhost000
from Core.eletter import Blockchain
from Core.eletter import Spotify
from Core.eletter import Rockstar
from Core.eletter import Dreamteam
from Core.eletter import Mega
from Core.eletter import RiotGames
from Core.eletter import Steam

from Core.eletter import GmailActivity
from Core.eletter import SnapchatSimple
from Core.eletter import Playstation
from Core.devicemenu import Linkedin
from Core.devicemenu import Dropbox
from Core.ipmenu import Discord
from Core.ipmenu import Paypal1
from Core.ipmenu import Snapchat
from Core.pre import *
from Core.helper.RedirectBypass import *
from rgbprint import gradient_print
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
blue = Fore.CYAN

os.system("clear")


def CurrentDir():
    path = os.getcwd()
    print(
        green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path + '/"TemplateName.html"')


no = ["n", "no"]
cont = ""
while cont not in no:
    def mainMenu():
        os.system("cls") if 'Windows' in platform.platform() else os.system('clear')
        menu()

        print(green)

        CurrentDir()

        mailPick = int(input(green + "root@CyberPhish ~> " + white))

        try:

            if mailPick == 1:
                Instagram()

            elif mailPick == 2:
                Facebook()

            elif mailPick == 3:
                Gmail()

            elif mailPick == 4:
                GmailActivity()

            elif mailPick == 5:
                Twitter()

            elif mailPick == 6:
                Snapchat()

            elif mailPick == 7:
                SnapchatSimple()

            elif mailPick == 8:
                Steam()

            elif mailPick == 9:
                Dropbox()

            elif mailPick == 10:
                Linkedin()

            elif mailPick == 11:
                Playstation()

            elif mailPick == 12:
                Paypal1()

            elif mailPick == 13:
                Discord()

            elif mailPick == 14:
                Spotify()

            elif mailPick == 15:
                Blockchain()

            elif mailPick == 16:
                RiotGames()

            elif mailPick == 17:
                Rockstar()

            elif mailPick == 18:
                AskFM()

            elif mailPick == 19:
                Webhost000()

            elif mailPick == 20:
                Dreamteam()

            elif mailPick == 22:
                Mega()

            elif mailPick == 69:
                RedirectionMain()

            elif mailPick == 00:
                os.system("cls") if 'Windows' in platform.platform() else os.system('clear')
                print("- Hope I See You Soon")
                print("- Happy Phishing")
                sys.exit()

            else:
                print("\n- Something Went Wrong There Partner")
                sys.exit()

        except ValueError:
            print("\nSomething Went Wrong There Partner")

            sys.exit()
        except KeyboardInterrupt:
            print("\nExiting tool....")
            Welcome()


    mainMenu()

    cont = input(red + "Do you want to continue? [y/n] :")
    if cont == "y":
        os.system("cls") if 'Windows' in platform.platform() else os.system('clear')
        menu()
