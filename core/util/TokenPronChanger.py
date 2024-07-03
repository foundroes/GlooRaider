from core.add.plugins import *


import threading
from time import sleep

def pronounceChanger():
    global success, failure
    success = 0
    failure = 0
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Token Pronoun Changer]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')
    pronouns = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}PRONOUNS{o}] {s}>{w} ")
    clpr()
    if pronouns == "" or pronouns == None:
        pronouns = "https://gloo.lol"
    else:
        pronouns = pronouns

    output_lock = threading.Lock()
    def pronoun_changer(token):
        global success, failure
        payload = {
            "pronouns": pronouns
        }

        headers = {
            'authorization': token,
            "accept": "*/*",
            "accept-language": "en-GB",
            "content-length": str(len(dumps(payload))),
            "content-type": "application/json",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": xsup
        }

        response = session.patch(f"https://discord.com/api/v9/users/@me/profile", headers=headers, json=payload)
        time_rn = get_time_rn()
        if response.status_code == 200:
            success +=1
            print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")
        else:
            failure +=1
            print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]")


    def process_token(token):
        pronoun_changer(token)

    def main():
        with open("Assets/Input/Tokens.txt", "r", encoding='utf-8') as f:
            tokens = f.read().splitlines()

        num_threads = get_num_threads()  # Getting number of threads from config.ini

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            executor.map(process_token, tokens)
    
    main() 
    clpr()

    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clpr()
        print(f"""                       {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Changed the pron. of the token in the server!
                       {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Failed to change the pron. of the token!""")
        input(f"\n                       {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")
    
    elif choose == "":
        pass