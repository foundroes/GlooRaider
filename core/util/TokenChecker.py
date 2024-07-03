import requests
import json
import sys
import ctypes
import threading
import datetime
import easygui
import configparser

from pystyle import Write, Colors
from core.add.plugins import *



def check_token(token, valid_tokens, locked_tokens, invalid_tokens, lock):
    time_rn = get_time_rn()
    try:
        response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "de-DE"})
        if response.status_code == 200:
            with lock:
                valid_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {lg}[{g}VALID{lg}]   {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")
        elif response.status_code == 403:
            with lock:
                locked_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {ly}[{y}LOCKED{ly}]  {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")
        elif response.status_code == 401:
            with lock:
                invalid_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {lr}[{r}INVALID{lr}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")
        else:
            print(f"                     {o}[{m}{time_rn}{o}] {ly}[{y}LIMITED{ly}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")
    except:
        with lock:
            locked_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {ly}[{y}LOCKED{ly}]  {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")

def tokenchecker():
    titles(title3)
    valid_tokens = []
    invalid_tokens = []
    locked_tokens = []
    lock = threading.Lock()
    
    num_threads = get_num_threads()
    
    clpr()

    path = "Assets/Input/Tokens.txt" 
    with open(path, "r") as f:
        tokens = [line.strip() for line in f.readlines()]
    
    threads = []
    for token in tokens:
        t = threading.Thread(target=check_token, args=(token, valid_tokens, locked_tokens, invalid_tokens, lock))
        threads.append(t)
        t.start()
        
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()


    with open("valid.txt", 'w', encoding="utf-8") as f:
        for token in valid_tokens:
            f.write(token + "\n")

    clpr()
    print(f"""                       {o}[{w}Type {o}"{m}show{o}"{w} for info or {o}"{m}check{o}"{w} to save valid token profile data{o}]\n""")
    choose = input(f"                        {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")


    if choose == "show":
        clpr()
        print(f"""                           {lg}[{g}VALID{lg}]   {s}| {o}[{m}{len(valid_tokens):03}{o}] {s}> {w}Token is valid and sorted in valid.txt.
                           {ly}[{y}LOCKED{ly}]  {s}| {o}[{m}{len(locked_tokens):03}{o}] {s}> {w}Token is email{o}/{w}phone locked.
                           {lr}[{r}INVALID{lr}] {s}| {o}[{m}{len(invalid_tokens):03}{o}] {s}> {w}Token is invalid.
""")
        input(f"                           {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back. ")   


    elif choose == "check": 
        clpr()
        print(f"                             {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {w}This is a premium version feature!")
        sleep(1)
        print(f"                             {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {w}Going back to the main menu...")
        sleep(1)
        pass
        
    elif choose == "":
        pass
