from core import *

def DiscordInvite():
    webbrowser.open('https://discord.gg/pqaYpfXDHj')

def Website():
    webbrowser.open('https://gloo.lol')

def Developer():
    webbrowser.open('https://lostroes.lol')

def Github():
    webbrowser.open('https://lostroes.sell.app')

def Socials():

    clearprint()

    print(f"""                                   {o}[{m}01{o}] {s}>{w} Discord          {o}[{m}03{o}] {s}>{w} Developer 
                                   {o}[{m}02{o}] {s}>{w} Website          {o}[{m}04{o}] {s}>{w} Store""")
    
    whichone = input(f"\n                                   {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INPUT{o}] {s}>{w} ")

    if whichone == "1":
        DiscordInvite()
    
    elif whichone == "2":
        Website()

    if whichone == "3":
        Developer()
    
    elif whichone == "4":
        Github()

    else:
        print(f"                                   {o}[{m}GLOO{o}] {s}|{w} {o}[{m}ERROR{o}] {s}>{w} Invalid Input, try again.")

