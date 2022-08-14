#This is a simple STEAM GiftCard generator Made by deez fat nutz
#Im new in coding, if u want to help me:https://discord.gg/fBwanttf7Z
import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
import colorama
from colorama import Fore, init, Style, Back
from datetime import date

os.system("title Steamcard Generator - ENIGMA#0420")
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Style.BRIGHT + Fore.GREEN + Back.BLACK +'HACKING-VALVE... '+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

os.system("cls")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.GREEN + Back.BLACK +"]"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"]")
print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         Welcome to "+Fore.GREEN+"Steamcard Generator")
print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [1] "+Fore.GREEN+"Format 1"+" XXXXX-XXXXX-XXXXX-XXXXX")
print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [2] "+Fore.GREEN+"Format 2"+" XXXXX-XXXXX-XXXXX")
print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [3] "+Fore.GREEN+"Credits")
print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [4] "+Fore.GREEN+"Exit")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.GREEN + Back.BLACK +"]"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"]")

opcion = int(input("Choice: "))

if opcion==1:
	os.system("cls")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                         ["+Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+Style.BRIGHT + Fore.GREEN + Back.BLACK +"]"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"["+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                                     SteamCard Generator"+Fore.RED+" Made by "+Fore.RED+"ENIGMA#0420")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                         ["+Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+Style.BRIGHT + Fore.GREEN + Back.BLACK +"]"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"["+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"]")
	cantidad = input(Style.BRIGHT + Fore.GREEN + Back.BLACK +"\nHow many giftcards want to generate: ")
	while(int(count)<int(cantidad)):
	    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	    f= open(current_path+"/"+str("Steamcards")+str("")+".txt","a")
	    f.write(Generated+"\n")
	    print(Style.BRIGHT + Fore.MAGENTA + Back.BLACK +""+Fore.MAGENTA + Generated)
	    count+=1
	input(Style.BRIGHT + Fore.GREEN +"\nCodes have been generated & saved!\nPress enter to exit.")
	pass

if opcion==2:
	os.system("cls")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                         ["+Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+Style.BRIGHT + Fore.GREEN + Back.BLACK +"]"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"["+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                                     Steamcard Generator"+Fore.RED+" Made by "+Fore.RED+"ENIGMA#0420")
	print(Style.BRIGHT + Fore.GREEN + Back.BLACK +"                         ["+Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+Style.BRIGHT + Fore.GREEN + Back.BLACK +"]"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"["+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"+"+ Style.BRIGHT + Fore.GREEN + Back.BLACK +"]")
	cantidad = input(Style.BRIGHT + Fore.GREEN + Back.BLACK +"\nHow many giftcards want to generate: ")
	while(int(count)<int(cantidad)):
	    Generated = random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits).upper() for _ in range(4))+"-"+random.choice(string.ascii_uppercase).upper()+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))+"-"+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
	    f= open(current_path+"/"+str("Steamcards")+str("")+".txt","a")
	    f.write(Generated+"\n")
	    print(Style.NORMAL + Fore.MAGENTA + Back.BLACK +""+Fore.MAGENTA + Generated)
	    count+=1
	input(Style.BRIGHT + Fore.GREEN+"\nCodes have been generated & saved!\nPress enter to exit.")
	pass

if opcion==3:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         Steamcard Generator"+Fore.RED+" Made by "+Fore.RED+"ENIGMA#0420")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [Github] "+Fore.RED+"https://github.com/ENIGMA2O5")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [Discord] "+Fore.RED+"ENIGMA#0420")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                         [Server] "+Fore.RED+"https://discord.gg/fBwanttf7Z")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	input(Style.BRIGHT + Fore.RED + Back.BLACK +"\nEnter to exit")
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                  Closing!")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass

if opcion==4:
	os.system("cls")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	print(Style.BRIGHT + Fore.RED + Back.BLACK +"                                                  Closing!")
	print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.BLUE + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
	time.sleep(2)
	sys.exit()
	pass
