import os
from colorama import Fore
red = "\033[1;31;40m"
green = "\033[1;32;40m"
white = "\033[1;37;40m"
blue = "\033[1;34;40m"
yellow = Fore.CYAN
purple = Fore.MAGENTA


start = (green + "[" + white + "+" + green + "]" + white)
alert = (green + "[" + red + "!" + green + "]" + white)

def numbering(num):
  return green + "[" + white + str(num) + green + "]"

def CurrentDir():
	path = os.getcwd()
	print(green + "[" + white + "+" + green + "]" + white + " Your Templates Will Be Saved Here " + path)
