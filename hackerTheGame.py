#!/usr/bin/python3.5

## Hacker - The Game
## Run and see About

## I'm going to make this game for fun
## and of course learn with it

## Dependences
##### mpv  -  https://github.com/mpv-player/mpv 

## import modules
import json

from time import sleep
from os import system, path

## Create Json File
data = {
            'user':{
                'name':'admin',
                'password':'12345'
            },
            'hardware':{
                'cpu':1,
                'ram':1,
                'internet':1
            },
            'software':{
                'anti_virus':1,
                'encrypt':1,
                'descrypt':1
            },
            'money':{
                'bit_coins':100
            }
       }


absolutePath = path.abspath(__file__)
dirname = path.dirname(absolutePath)

try:
    open(dirname + "/info.json", "r")
except FileNotFoundError:
    with open(dirname + "/info.json", "w") as infoFile:
        json.dump(data, infoFile)

## Colors
class color:
    reset = "\033[00m"

    red         = "\033[0;31m"
    green       = "\033[0;32m"
    yellow      = "\033[0;33m"
    dark_blue   = "\033[0;34m"
    purple      = "\033[0;35m"
    light_blue  = "\033[0;36m"
    white       = "\033[0;37m"

    class bold:
        red         = "\033[1;31m"
        green       = "\033[1;32m"
        yellow      = "\033[1;33m"
        dark_blue   = "\033[1;34m"
        purple      = "\033[1;35m"
        light_blue  = "\033[1;36m"
        white       = "\033[1;37m"

## Features
class feature:
    italic       = "\033[3m"
    underline    = "\033[4m"
    alert        = "\033[5m"
    background   = "\033[7m"

## Title of the game
gameTitle = color.bold.red + \
        "░█░█░█▀█░█▀▀░█░█░█▀▀░█▀▄░░░░░░░░░▀█▀░█░█░█▀▀░░░█▀▀░█▀█░█▄█░█▀▀\n" \
        "░█▀█░█▀█░█░░░█▀▄░█▀▀░█▀▄░░░▄▄▄░░░░█░░█▀█░█▀▀░░░█░█░█▀█░█░█░█▀▀\n" \
        "░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░░░░░░░░░▀░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀\n" + color.reset

## Main menu of the game
def startMenu(option):
    anwser = option

    system("clear")
    print(gameTitle)

    ## Options in main Menu
    print(color.bold.green + " [0] " + color.bold.white + "-" + color.bold.yellow + " Quit ")
    print(color.bold.green + " [1] " + color.bold.white + "-" + color.bold.yellow + " Play ")
    print(color.bold.green + " [2] " + color.bold.white + "-" + color.bold.yellow + " About \n")

    if anwser == None: anwser = input(color.reset + "> ")
    return anwser

## About
def aboutMenu(option):
    anwser = option

    system("clear")
    print(gameTitle)

    aboutText = " This game has created to study \n" \
                " created in python3.5 by me \n" \
                " I chose the title 'Hacker - The Game' because... \n" \
                " I'm a hacker. \n"

    print(color.bold.light_blue + aboutText)

    ## Options in AboutMenu
    print(color.bold.green + " [0] " + color.bold.white + "-" + color.bold.yellow + " Quit ")
    print(color.bold.green + " [1] " + color.bold.white + "-" + color.bold.yellow + " Back \n")

    if anwser == None: anwser = input(color.reset + "> ")
    return anwser

def login():
    with open(dirname + "/info.json", "r") as infoFile:
        info = json.load(infoFile)

    if info["user"]["name"] == "admin" and info["user"]["password"] == "12345":
        print(color.bold.red + " Not use Login: admin and password: 12345 \n" + color.reset)

        name = input("Choose a name: ")
        password = input("Choose a password: ")

        info["user"]["name"] = name
        info["user"]["password"] = password

        with open(dirname + "/info.json", "w") as infoFile:
            json.dump(info, infoFile)

        quit()
    else:
        loginName = input("name: ")
        loginPassword = input("password: ")

        if loginName == info["user"]["name"] and loginPassword == info["user"]["password"]:
            return True

def missions(mission):
    if mission == "1":
        print(color.bold.light_blue + "  Misson 1: Invade the server local")
        print(color.bold.purple + "     invade the server local and exit \n")
        
        print(color.red + " type this 127.0.0.1\n" + color.reset)
        
        print(color.bold.red + "root@linux" + color.bold.white + ": /" + color.reset + " # ", end="")
        anwser = input("nmap -A -T4 ")

        if anwser == "127.0.0.1":
            print(color.bold.green)
            print(" Starting Nmap Scan on '127.0.0.1' wait...")
            sleep(2)
            print(" Scan Ports...")
            sleep(0.1)
            print(" Scan OS...\n")
            sleep(0.1)

            print(" PORTS        STATE       SERVICE")
            
            line1 = " 22/tcp       open        http        hack.net"
            line2 = " 80/tcp       open        http        linux-GNU"
            line3 = " 2222/tcp     close       ftp         nsa.org\n"
            
            for i in line1, line2, line3:
                print(i)
                sleep(0.1)

            sleep(0.1)

            print("OS:")
            line1 = "|   GNU/Linux:"
            line2 = "|      192.198.5.2:"
            line3 = "|         Version:"
            line4 = "|           name: Arch Linux"
            line5 = "|           kernel: 4.15.2-ARCH"
            line6 = "|           site: archlinux.org"
            line7 = "|         TCP PORTS:"
            line8 = "|           22     <open>"
            line9 = "|           80     <open>"
            line10 = "|           2222   <close>\n"
            
            for i in line1, line2, line3, line4, line5, line6, line7, line8, line9, line10:
                print(i)
                sleep(0.1)

            sleep(1)

            print("Nmap done: 1 IP address (1 host up), 2 ports open, 1 OS detected")
            print(color.reset)

            print(color.bold.green + feature.background + feature.alert + " " * 20, "Congratulations" + " " * 20, "\n" + color.reset)
            
            with open(dirname + "/info.json", "r") as infoFile:
                info = json.load(infoFile)

            info["money"]["bit_coins"] += 100

            with open(dirname + "/info.json", "w") as infoFile:
                json.dump(info, infoFile)

        else:
            print(anwser, color.bold.red + "is not a valid IP" + color.reset)

    elif mission == "2":
        print(color.bold.light_blue + "  Mission 2: Descrypt morse code")
        print(color.bold.purple + "     you'll hear a morse code, try descrypt it \n")

        print(color.bold.green + "Playing... \n\n ", end="")
        sleep(1)
        
        ## Play audio in background
        system("mpv '" + dirname + "/sound/morse.wav' &> /dev/null &")

        ## Hide cursor 
        system("setterm -cursor off")
        
        ## Visual progress bar for audio
        for i in range(1,30):
            print(color.bold.light_blue + "━", end="", flush=True)
            sleep(0.14)

        sleep(1)

        print(color.reset + color.bold.red + "\n\n what the morse code say?" + color.reset)
        
        ## Back cursor
        system("setterm -cursor on")
        
        anwser = input("> ")

        ## just see it if you are a noob :P
        if anwser == "best game":
            print()
            print(color.bold.green + feature.background + feature.alert + " " * 20, "Congratulations" + " " * 20, "\n" + color.reset)

            with open(dirname + "/info.json", "r") as infoFile:
                info = json.load(infoFile)

            info["money"]["bit_coins"] += 100

            with open(dirname + "/info.json", "w") as infoFile:
                json.dump(info, infoFile)

        else:
            print()
            print(color.bold.red + feature.background + feature.alert + " " * 20, "NOOB, try again" + " " * 20, "\n" + color.reset)
            sleep(1)
            missions("2")

def playMenu():
    print(color.bold.green + " [0] " + color.bold.white + "-" + color.bold.yellow + " Quit ")
    print(color.bold.green + " [1] " + color.bold.white + "-" + color.bold.yellow + " Hardware ")
    print(color.bold.green + " [2] " + color.bold.white + "-" + color.bold.yellow + " Software ")
    print(color.bold.green + " [4] " + color.bold.white + "-" + color.bold.yellow + " Missions \n" + color.reset)

    anwser = input("> ")

    if anwser == "0":
        quit()
    elif anwser == "1":
        print("nothing")
    elif anwser == "2":
        print("nothing")
    elif anwser == "3":
        print("nothing")
    elif anwser == "4":
        print(color.bold.green + "<1>" + color.bold.white + " -- " + color.bold.light_blue + " Scan Localhost ")
        print(color.bold.green + "<2>" + color.bold.white + " -- " + color.bold.light_blue + " Descrypt Morse Code \n" + color.reset)

        mission = input("Choose the mission: ")

        missions(mission)
    else:
        print("error: no option: ", anwser)
        sleep(1)
        menu("1")

## The Game
def main():
    system("clear")
    print(gameTitle)

    print(color.green + " Booting Device: \n")
    
    ## Hide Cursor
    system("setterm -cursor off")

    ## Progress Bar
    print("   " , end="")
    
    for i in range(0,30):
        print(color.bold.green + feature.background + " ", end="", flush=True)
        sleep(0.03)

    ## Game
    sleep(1)
    
    print(color.green + feature.underline + "\n\n Welcome to the Hacker Area \n" + color.reset)

    ## Back Cursor
    system("setterm -cursor on")
    
    ## Login
    loginResult = login()

    if loginResult != True:
        print(color.bold.red + "\n Access Denied \n")
        sleep(1)
        main()
    
    with open(dirname + "/info.json", "r") as infoFile:
        info = json.load(infoFile)

    name = info["user"]["name"]
    coins = info["money"]["bit_coins"]
    
    print(color.bold.green + "\n Welcome, " + name)
    print(color.bold.red + "    Status - Name: " + name + ", BitCoins: ", coins, "\n")

    playMenu()

## Menu
def menu(option):
    firstMenu = startMenu(option)

    if firstMenu == "0":
        quit()
    elif firstMenu == "1":
        main()
    elif firstMenu == "2":
        secondMenu = aboutMenu(None)
        
        if secondMenu == "0":
            quit()
        elif secondMenu == "1":
            menu(None)
        else:
            print("error: no option:", secondMenu)
            sleep(1)
            menu("2")
    else:
        print("error: no option:", firstMenu)
        sleep(1)
        menu(None)

## Run Menu
menu(None)
