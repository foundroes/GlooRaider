
from core import *


def check_token(token, valid_tokens, locked_tokens, invalid_tokens, lock):
    time_rn = getting.get_time_rn()
    try:

        session = Client.get_session(token)

        response = session.get('https://discord.com/api/v9/users/@me/library')

        if response.status_code == 200:
            with lock:
                valid_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {lg}[{g}VALID{lg}]   {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]{d}")
        elif response.status_code == 403:
            with lock:
                locked_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {ly}[{y}LOCKED{ly}]{y}  {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]{d}")
        elif response.status_code == 401:
            with lock:
                invalid_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {lr}[{r}INVALID{lr}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]{d}")
        else:
            print(f"                     {o}[{m}{time_rn}{o}] {ly}[{y}LIMITED{ly}]{y} {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]{d}")
    except Exception as e:
        with lock:
            locked_tokens.append(token)
            print(f"                     {o}[{m}{time_rn}{o}] {ly}[{y}LOCKED{ly}]{y}  {s}|{w} {token[:37]} {o}[{m}Error{e}{o}]{d}")

def Checker():
    titles('CHECKER')
    valid_tokens = []
    invalid_tokens = []
    locked_tokens = []

    num_threads = getting.get_num_threads()  
    
    clearprint()

    tokens = getting.get_tokens()
    
    threads = []
    for token in tokens:
        t = threading.Thread(target=check_token, args=(token, valid_tokens, locked_tokens, invalid_tokens, lock))  # Passing arguments as args tuple
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

    clearprint()
    print(f"""                         {o}[{w}Type {o}"{m}show{o}"{w} for info or {o}"{m}check{o}"{w} to save token profile data{o}]\n""")
    choose = input(f"                          {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":  
        clearprint()
        print(f"""                          {lg}[{g}VALID{lg}]   {s}| {o}[{m}{len(valid_tokens):03}{o}] {s}> {w}Token is valid and stored in valid.txt.
                          {ly}[{y}LOCKED{ly}]{y}  {s}| {o}[{m}{len(locked_tokens):03}{o}] {s}> {w}Token is email/phone locked.
                          {lr}[{r}INVALID{lr}] {s}| {o}[{m}{len(invalid_tokens):03}{o}] {s}> {w}Token is invalid.
""")
        input(f"                          {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back. ")   

    elif choose == "check":
        Premium()
