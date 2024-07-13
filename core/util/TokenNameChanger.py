from core.add.plugins import *


import threading
from time import sleep


def namechanger():
    global success, failure
    success = 0
    failure = 0
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Token Nickname Changer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')
    
    def changenick(server, nickname, token):
        global success, failure
        time_rn = getting.get_time_rn()
        headers = getting.get_headers(token)
        response = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers, json={"nick": nickname})
        if response.status_code == 200:
            success +=1
            print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")
        else:
            failure +=1
            print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")

    
    tokens = getting.get_tokens()
    server = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}GUILD ID{o}] {s}>{w} ")
    nick = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}USERNAME{o}] {s}>{w} ")
    clear()
    print(toolprint)
    print("")

    # Getting number of threads from config.ini
    num_threads = getting.get_num_threads()
    
    path = "Assets/Input/Tokens.txt" 
    with open(path, "r") as f:
        tokens = [line.strip() for line in f.readlines()]
    
    threads = []
    for token in tokens:
        t = threading.Thread(target=changenick, args=(server, nick, token)) 
        threads.append(t)
        t.start()
        
        # Limit number of concurrent threads
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []
    
    for t in threads:
        t.join()
    
    clearprint()

    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clearprint()
        print(f"""                       {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Changed the name of the token in the server!
                       {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Failed to change the name of the token!""")
        input(f"\n                       {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")
    
    elif choose == "":
        pass
