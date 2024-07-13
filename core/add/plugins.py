import os
import sys
import json
import time
import pytz
import httpx
import base64
import string
import ctypes
import asyncio
import sys
import os
import webbrowser
import random
import easygui
import discord
import asyncio
import secrets
import requests
import websocket
import threading
import tls_client
import concurrent
import winreg
import concurrent.futures
import io
import re
import shutil
import os.path
import zipfile
import importlib
import subprocess
from distutils.version      import LooseVersion
from pystyle                import *
from dhooks import Webhook
from time                   import sleep
from json import loads
from discord.ext import commands
from colorama               import init, Fore
from requests import session
from bs4                    import BeautifulSoup
from urllib.request         import urlopen, urlretrieve
import datetime
from time import sleep
from genericpath import isfile
from websocket import WebSocket
from json import dumps
from ntpath import join
from requests import Session
from concurrent.futures import ThreadPoolExecutor
from twocaptcha import TwoCaptcha
import configparser
from colorama import init
import colorama 
from core.add.plugins import *
init()

class getting:
    def get_tokens():
        with open("assets/input/tokens.txt", "r") as file:
            tokens = file.readlines()
            return tokens

    def get_num_threads():
        config = configparser.ConfigParser()
        config.read('config.ini')  
        return int(config['MAIN']['threads'])

    def load_config():
        config = configparser.ConfigParser()
        config.read("config.ini")
        status_rotater_config = config["STATUS"]
        debug_config = config["DEBUG"]
        return {
            "status_rotater": {
                "token": status_rotater_config["token"],
                "sleep_interval": status_rotater_config["sleep_interval"] 
            },
            "debug": {
                "clear_enabled": debug_config.getboolean("clear_enabled"),
                "clear_interval": debug_config.getint("clear_interval"),
            }
        }
    
    def get_time_rn():
        date = datetime.datetime.now()
        hour = date.hour
        minute = date.minute
        second = date.second
        timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
        return timee

    def read_config():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config

    def randstr(lenn):
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        text = ''
        for i in range(0, lenn):
            text += alpha[random.randint(0, len(alpha) - 1)]
        return text
    

    def get_cookie(): 
        response = requests.Session().get('https://discord.com/app')
        cookie = str(response.cookies)
        return cookie.split('dcfduid=')[1].split(' ')[0], cookie.split('sdcfduid=')[1].split(' ')[0], cookie.split('cfruid=')[1].split(' ')[0]

    def get_headers(token):
        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "en-US",
            "authorization": token,
            "cookie": "__dcfduid=%s; __sdcfduid=%s; locale=en-US; __cfruid=%s" % getting.get_cookie(),
            "connection": "keep-alive",
            "content-type": "application/json",
            "origin": "https://discord.com",
            "referer": "https://discord.com/",
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-discord-timezone": "America/New_York",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDExIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTc5ODgyLCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozMDMwNiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
        }
        return headers

class validate:
    def checkfortokens():
            clearprint()
            print(f"                                 {o}[{w}No tokens found in {dirchecker}{o}]")
            input(f"\n                                  {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")

    def validateWebhook(hook):
        if not "api/webhooks" in hook:
            clearprint()
            print(f"\n                                  {o}[{w}Invalid webhook, failed to run the tool{o}]")
            sleep(2)
            pass

    def validatetoken(token):
        response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "de-DE"})
        if response.status_code == 200:
            pass
        else:
            clearprint()
            print(f"                                  {o}[{w}Your token is invalid, please try again{o}]")
            sleep(2)
            pass

def clear():
    os.system("cls")

def titles(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def generate_color_shades(color):

    color_codes = {
        'blue': [69, 63, 62, 61, 60, 59], 
        'red': []

    }
   
    shades = color_codes.get(color, [])
    if shades:

        return [f"\x1b[38;5;{shade}m" for shade in shades]
    else:
        print("Unsupported color.")
        return []
    
def colorize_text(text, color_shades):
    colored_text = ""
    for i, char in enumerate(text):
        colored_text += f"{cs[i % len(color_shades)]}{char}"
    return colored_text

def discord():
    webbrowser.open('https://discord.com/invite/uJE9rfJ7Tz')

def website():
    webbrowser.open('https:/gloo.lol')


config = configparser.ConfigParser()
config.read('config.ini')

color = config.get('THEMES', 'color')
cs = generate_color_shades(color) 

u = "\x1b[38;5;69m"
i = "\x1b[38;5;63m"
p = "\x1b[38;5;62m"
o = "\x1b[38;5;61m"
m = "\x1b[38;5;60m"
k = "\x1b[38;5;59m"
free = "\x1b[38;5;234m"

s = Fore.LIGHTBLACK_EX
w = Fore.WHITE

r = Fore.RED
ur = "\x1b[4;31m"
lr = Fore.LIGHTRED_EX

g = Fore.GREEN
ug = "\x1b[4;32m"
lg = Fore.LIGHTGREEN_EX

y = Fore.YELLOW
uy = "\x1b[4;33m"
ly = "\x1b[38;5;178m"

b = "\x1b[38;5;69m"
lb = Fore.LIGHTBLUE_EX

chrome_version = "116"
xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

session = tls_client.Session(
    client_identifier="chrome_116",
)

dirchecker = 'assets/input/tokens.txt'
counttokens = len(open(dirchecker).readlines())
countproxies = len(open('assets/input/proxies.txt').readlines())
toolprint = f"""{free}[OPEN SOURCE - FREE VERSION]

{cs[0]}                                             __                  __      __
{cs[1]}                                      ____  / /___  ____        / /___  / /
{cs[2]}                                     / __ `/ / __ \/ __ \      / / __ \/ / 
{cs[3]}                                    / /_/ / / /_/ / /_/ / __  / / /_/ / /  
{cs[4]}                                    \__, /_/\____/\____/ /_/ /_/\____/_/   
{cs[5]}                                   /____/                          
"""
def clearprint():
    clear()
    print(toolprint)

mainpage = f"""       {o}[{m}01{o}] {s}> {w}Token Formater  {o}[{m}06{o}] {s}> {w}Token Dupe. Remover   {o}[{m}11{o}] {s}> {w}Webhook Spammer  {o}[{m}16{o}] {s}> {w}Sound Spammer
       {o}[{m}02{o}] {s}> {w}Token Checker   {o}[{m}07{o}] {s}> {w}Token Pron. Changer   {o}[{m}12{o}] {s}> {w}Webhook Deleter  {o}[{m}17{o}] {s}> {w}Audit Spammer
       {o}[{m}03{o}] {s}> {w}Token Onliner   {o}[{m}08{o}] {s}> {w}Token Custom Status   {o}[{m}13{o}] {s}> {w}Webhook Lookup   {o}[{m}18{o}] {s}> {w}Website
       {o}[{m}04{o}] {s}> {w}Token Leaver    {o}[{m}09{o}] {s}> {w}Token Name Changer    {o}[{m}14{o}] {s}> {w}Channel Spammer  {o}[{m}19{o}] {s}> {w}Discord
       {o}[{m}05{o}] {s}> {w}Token Info      {o}[{m}10{o}] {s}> {w}Token Bio Changer     {o}[{m}15{o}] {s}> {w}Basic Spammer    {o}[{m}20{o}] {s}> {w}Exit"""


title1 =  f'[Gloo Raider]  |  [Token Formater]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title2 =  f'[Gloo Raider]  |  [Token Checker]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title3 =  f'[Gloo Raider]  |  [Token Onliner]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title4 =  f'[Gloo Raider]  |  [Token Guild Leaver]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title5 =  f'[Gloo Raider]  |  [Token Info]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title6 =  f'[Gloo Raider]  |  [Token Duplicate Remover]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'  
title7 =  f'[Gloo Raider]  |  [Token Pronouns Changer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title8 =  f'[Gloo Raider]  |  [Token Name Changer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title9 =  f'[Gloo Raider]  |  [Token Bio Changer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title10 = f'[Gloo Raider]  |  [Token Custom Status]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title11 = f'[Gloo Raider]  |  [Webhook Spammer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title12 = f'[Gloo Raider]  |  [Webhook Deleter]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title13 = f'[Gloo Raider]  |  [Webhook Lookup]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title14 = f'[Gloo Raider]  |  [Channel Spammer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title15 = f'[Gloo Raider]  |  [Basic Spammer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title16 = f'[Gloo Raider]  |  [Sound Spammer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'
title17 = f'[Gloo Raider]  |  [Audit Spammer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]'

nicknames = [
    "ShadowStriker",
    "CyberNinja",
    "ThunderPulse",
    "VortexViper",
    "NovaKnight",
    "QuantumQuasar",
    "FrostbyteFury",
    "PixelProwler",
    "InfernoWraith",
    "MysticMarauder",
    "ZeroGravityGamer",
    "NeonNebula",
    "StarlightSpecter",
    "StormBreaker",
    "BlazeBanshee",
    "CosmicCrusader",
    "PhantomFury",
    "SilverSpectre",
    "TitanThunder",
    "WickedWraith",
    "EclipseEnigma",
    "VelocityVirtuoso",
    "OmegaOracle",
    "ZenithZealot",
    "RogueRevenant",
    "CelestialCenturion",
    "QuantumQuake",
    "IgnitionInferno",
    "ReaperRogue",
    "VelocityViper",
    "FrostFirePhoenix",
    "LunarLynx",
    "QuantumQuasar",
    "AbyssalAvenger",
    "NebulaNemesis",
    "ZeroZephyr",
    "SolarStorm",
    "CrypticCobra",
    "DarkDemon",
    "BlizzardBanshee",
    "GalacticGuardian",
    "ThunderTwilight",
    "StormySentinel",
    "NebulaNomad",
    "BlazeBolt",
    "ValkyrieVortex"]


yeslist = {"yes", 
           "y", 
           "yer", 
           "yeah",
           "yessir",
           "ye",
           "okay",
           "yep",
           "yea",
           "ok",
           "k",
           "yh",
           "sure"}

nolist = {"no", 
          "n", 
          "ner", 
          "nope",
          "nosir",
          "nah",
          "notokay",
          "noup",
          "na",
          "not",
          "nh",
          "nt"}
          
