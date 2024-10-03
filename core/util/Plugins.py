
import io
import os
import re
import sys
import time
import ctypes
import random
import webbrowser
import psutil
import shutil
import zipfile
import hashlib
import asyncio
import logging
import discord
import datetime
import requests
import threading
import tls_client
import configparser

from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep
from pystyle import System
from distutils.version import LooseVersion
from psutil import Process, virtual_memory, cpu_count, disk_usage
from win32gui import GetWindowText, EnumWindows
from win32process import GetWindowThreadProcessId
from winreg import HKEY_LOCAL_MACHINE, OpenKey, CloseKey, QueryValueEx
from urllib.request import urlretrieve

System.Size(110, 20)

lock = threading.Lock()

GUILD = "1157804609197326376"

def Premium():
    clearprint()
    print(f'                          {o}[{w}This is a Premium feature, do you want to check it out{o}]')

    checkPremium = input(f'\n                           {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} {d}')

    if checkPremium in yeslist:
        webbrowser.open('https://lostroes.sell.app')

    else:
        pass



#----------------------------------------------------------#

class getting:
            
    def get_time_rn(): #-----# Time Print
        date = datetime.datetime.now()
        hour = date.hour
        minute = date.minute
        second = date.second
        timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
        return timee

    def get_tokens():  # ------# Get Tokens
        with open("assets/input/tokens.txt", "r", encoding='utf-8') as file:
            tokens = file.read().splitlines()  # strip newline characters
            return tokens
        
    def get_num_threads(): #-# Get Threads
        config = configparser.ConfigParser()
        config.read('config.ini')  
        return int(config['MAIN']['threads'])

    def getTempDir(): #------# Get Temp Directory
        system = os.name
        if system == 'nt':
            return os.getenv('temp')
        elif system == 'posix':
            return '/tmp/'
        
class addons:

    tokenoptions = {
        '1': True, 
        '3': True, 
        '4': True, 
        '6': True, 
        '7': True, 
        '8': True, 
        '9': True, 
        '12': True, 
        '13': True,  
        '15': True, 
        '16': True, 
        '20': True, 
        '21': True, 
        '23': True, 
        '24': True, 
        '25': True, 
        '26': True, 
        '27': True, 
        '28': True, 
        '29': True,
        '35': True
    }

    @staticmethod
    def checkfortokens(option=None):
        if option in addons.tokenoptions:
            clearprint()
            print(f"                                 {o}[{w}No tokens found in {checktokens}{o}]")
            input(f"\n                                  {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        else:
            pass

    def validateWebhook(hook):
        if not "api/webhooks" in hook:
            clearprint()
            print(f"                                  {o}[{w}Invalid webhook, failed to run the tool{o}]")
            sleep(2)
            
    def validatetoken(token):

        response = requests.get(
            'https://discord.com/api/v9/users/@me/library',
            headers={
                "authorization": token,
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
                "x-discord-locale": "de-DE"
            }
        )

        if response.status_code == 200:
            return True  # Explicitly return True if the token is valid
        else:
            with lock:
                clearprint()
                print(f"                                {o}[{w}Token is invalid. Try again with a newer one{o}]")
                input(f"\n                                 {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")
            return False  # Explicitly return False if the token is invalid

#----------------------------------------------------------#

configpath = 'config.ini'

def load_config():
    config_data = {}
    if os.path.exists(configpath):
        config = configparser.ConfigParser()
        config.read(configpath)
        
        for section in config.sections():
            config_data[section] = dict(config.items(section))
    
    return config_data
    
config = load_config()

directorypath = 'assets/input/'
checktokens = 'assets/input/tokens.txt'
checkids = 'assets/input/member_ids.txt'
checkproxies = 'assets/input/proxies.txt'

if os.path.exists(directorypath):
    counttokens = len(open(checktokens).readlines())
    countproxies = len(open(checkproxies).readlines())
    countmemberids = len(open(checkids).readlines())
else:
    pass


#----------------------------------------------------------#

def terminaltheme(color): # Terminal Text Themes
    color_codes = {            
        'default': [69,  63,  62,  61,  60,  59], 
        'blue':    [33,  27,  26,  25,  24,  23],
        'pink':    [141, 135, 134, 133, 132, 131],
        'green':   [123, 117, 116, 115, 114, 113],
        'purple':  [124, 125, 126, 127, 128, 129],
        'white':   [238, 239, 240, 241, 242, 243],
    }
   
    shades = color_codes.get(color, [])
    if shades:
        return [f"\x1b[38;5;{shade}m" for shade in shades]
    else:
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o} {s}>{w} Unsupported color.")
        return []

color = config['UI']['color']
cs = terminaltheme(color) # Colors

#----------------------------# DARK

o = f'{cs[3]}'
m = f'{cs[4]}'
d = Fore.BLACK
w = Fore.WHITE
r = Fore.RED
g = '\x1b[38;5;2m'
y = "\x1b[38;5;178m"
b = "\x1b[38;5;69m"

sx, sxs, sxsx = 20,20,20  
l = f"\033[38;2;{sx};{sxs};{sxsx}m"

#----------------------------# LIGHT

s = Fore.LIGHTBLACK_EX
lr = Fore.LIGHTRED_EX
lg = '\x1b[38;5;10m'
ly = '\x1b[38;5;220m'
lb = Fore.LIGHTBLUE_EX

#----------------------------------------------------------#

def clear(): #------------# Clear Terminal
    os.system("cls")

def clearprint(): #-------# Clear + Print
    clear()
    print(toolprint)

#----------------------------------------------------------#

edge_target_ver = 0 

class Edge_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://msedgedriver.azureedge.net/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = "edgedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = self._base.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            try:
                self.fetch_edgedriver()
                if not self.__class__.installed:
                    if self.patch_binary():
                        self.__class__.installed = True
            except Exception as e:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}EDGE{o}] {s}>{w} Error installing driver.")
        
    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open("ms"+self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect

    def get_release_version_number(self):
        path = (
            "LATEST_STABLE"
            if not self.target_version
            else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
        )
        try:
            urlretrieve(
                f"{self.__class__.DL_BASE}{path}",
                filename=f"{getting.getTempDir()}\\{path}",
            )
            with open(f"{getting.getTempDir()}\\{path}", "r+") as f:
                _file = f.read().strip("\n")
                content = ""
                for char in [x for x in _file]:
                    for num in ("0","1","2","3","4","5","6","7","8","9","."):
                        if char == num:
                            content += char
            return LooseVersion(content)
        except Exception as e:
            clearprint()
            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}EDGE{o}] {s}>{w} Error getting version.")

    def fetch_edgedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        try:
            urlretrieve(
                f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
                filename=zip_name,
            )
            with zipfile.ZipFile(zip_name) as zf:
                zf.extract("ms"+self._exe_name)
            os.remove(zip_name)
            if sys.platform != "win32":
                os.chmod(self._exe_name, 0o755)
            return self._exe_name
        except Exception as e:
            clearprint()
            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}EDGE{o}] {s}>{w} Error fetching driver.")

class Opera_Installer(object):
    DL_BASE = "https://github.com"
    
    def __init__(self, *args, **kwargs):
        self.platform = sys.platform
        self.links = ""

        try:
            r = requests.get(self.__class__.DL_BASE+"/operasoftware/operachromiumdriver/releases")
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all('a'):
                if "operadriver" in link.get('href'):
                    self.links += f"{link.get('href')}\n"

            for i in self.links.split("\n")[:4]:
                if self.platform in i:
                    self.fetch_operadriver(i)
        except Exception as e:
            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}OPERA{o}] {s}>{w} Error installing driver.")

    def fetch_operadriver(self, driver):
        try:
            executable = "operadriver.exe"
            driver_name = driver.split("/")[-1]
            cwd = os.getcwd() + os.sep

            urlretrieve(self.__class__.DL_BASE+driver, filename=driver_name)
            with zipfile.ZipFile(driver_name) as zf:
                zf.extractall()
            shutil.move(cwd+driver_name[:-4]+os.sep+executable, cwd+executable)
            os.remove(driver_name)
            shutil.rmtree(driver_name[:-4])
        except Exception as e:
            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}OPERA{o}] {s}>{w} Error fetching driver.")

def getDriver():
    try:

        drivers = ["msedgedriver.exe", "operadriver.exe"]
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Checking for Drivers..")
        sleep(0.5)
        for driver in drivers:
            if os.path.exists(os.getcwd() + os.sep + driver):
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} {driver.capitalize()} is already installed.")
                sleep(0.5)
                return driver
        else:
            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Installing Drivers..")
            if os.path.exists(os.getenv('appdata') + '\\Opera Software\\Opera Stable'):
                Opera_Installer()
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}OPERA{o}] {s}>{w} Installed operadriver.exe!")
                return "operadriver.exe"
            elif os.path.exists(os.getenv('localappdata') + '\\Microsoft\\Edge'):
                Edge_Installer()
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}EDGE{o}] {s}>{w} Installed msedgedriver.exe!")
                return "msedgedriver.exe"
            else:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} No driver found! Exiting.")
                
    except Exception as e:
        clear()
        print(f"{o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} {e}")

#----------------------------------------------------------#


def titles(title): #------# Titles
    if title in tooltitles:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]   |   [{tooltitles[title]}]   |   [Tokens: {counttokens}]   |   [Proxies: {countproxies}]   |   [https://gloo.lol]')
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]   |   [Tokens: {counttokens}]   |   [Proxies: {countproxies}]   |   [https://gloo.lol]')

tooltitles = { 
    'PAGE1': 'Page One',
    'PAGE2': 'Page Two',

    'FORMATTER': 'Token Formatter',
    'DISABLER': 'Token Disabler',
    'CHECKER': 'Token Checker',
    'ONLINER': 'Token Onliner',
    'GRABBER': 'Token Grabber',

    'PRON': 'Token Pronouns Changer',
    'TGJoiner': 'Token Guild Joiner',
    'TGLeaver': 'Token Guild Leaver',
    'NAME': 'Token Name Changer',
    'BIO': 'Token Bio Changer',

    'DUPE': 'Token Duplicate Remover',
    'REQSP': 'Friend Request Spammer',
    'CHANNEL': 'Channel Spammer',
    'GROUP': 'Group Spammer',
    'REPLY': 'Reply Spammer',

    'TNUKER': 'Token Nuker',
    'LOGIN': 'Token Login',
    'TINFO': 'Token Info',
    'REPLY': 'Reply Spammer',
    'SINFO': 'Server Info',
}

#----------------------------------------------------------#

toolprint = f"""

{cs[0]}                                             __                  __      __
{cs[1]}                                      ____  / /___  ____        / /___  / /
{cs[2]}                                     / __ `/ / __ \/ __ \      / / __ \/ / 
{cs[3]}                                    / /_/ / / /_/ / /_/ / __  / / /_/ / /  
{cs[4]}                                    \__, /_/\____/\____/ /_/ /_/\____/_/   
{cs[5]}                                   /____/                          
"""

page1menu = f"""     {o}[{m}01{o}]{m} {s}> {w}Token Formatter {o}[{m}06{o}]{m} {s}> {w}Token Pron. Changer  {o}[{m}11{o}]{m} {s}> {w}Token Dupe Remover   {o}[{m}16{o}]{m} {s}> {w}Token Nuker
     {o}[{m}02{o}]{m} {s}> {w}Token Disabler  {o}[{m}07{o}]{m} {s}> {w}Token Guild Joiner   {o}[{m}12{o}]{m} {s}> {w}Friend Req Spammer   {o}[{m}17{o}]{m} {s}> {w}Token Login
     {o}[{m}03{o}]{m} {s}> {w}Token Checker   {o}[{m}08{o}]{m} {s}> {w}Token Guild Leaver   {o}[{m}13{o}]{m} {s}> {w}Channel Spammer      {o}[{m}18{o}]{m} {s}> {w}Token Info
     {o}[{m}04{o}]{m} {s}> {w}Token Onliner   {o}[{m}09{o}]{m} {s}> {w}Token Name Changer   {o}[{m}14{o}]{m} {s}> {w}Group Spammer        {o}[{m}19{o}]{m} {s}> {w}Guild Info
     {o}[{m}05{o}]{m} {s}> {w}Token Grabber   {o}[{m}10{o}]{m} {s}> {w}Token Bio Changer    {o}[{m}15{o}]{m} {s}> {w}Reply Spammer        {o}[{m}20{o}]{m} {s}> {w}Socials"""

yeslist = {"yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure", "Y"}

nolist = {"no", "n", "ner", "nope","nosir","nah","notokay","noup","na","not","nh","nt", "N"}

emojilist = [
    '😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😇', '😈', '😉', '😊', '😋', '😌', 
    '😍', '🥰', '😘', '😗', '😙', '😚', '😜', '😝', '😛', '🤑', '🤗', '🤔', '🤭', '🤫', 
    '🤥', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', 
    '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', 
    '😓', '🤗', '🙄', '😶', '😐', '😑', '😬', '🤨', '🤢', '🤮', '🤧', '😷', '🥴', '😴',
    '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']

