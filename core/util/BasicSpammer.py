from core.add.plugins import *

import requests
import threading

def BasicSpammer():
    global success, failure
    failure = 0
    success = 0
    titles(title15)

    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}CHANNEL ID{o}] {s}>{w} ", end=""); channel_id = input()
    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MESSAGE{o}] {s}>{w} ", end=""); message = input()

    clpr()
    tokens = open("Assets/Input/Tokens.txt", "r").read().splitlines()

    num_threads = get_num_threads()  
    
    def spam(channel_id, message):
        global success, failure
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        data = {"content": message}
        for token in tokens:
            header = {"authorization": token}
            response = requests.post(url, data=data, headers=header)
            if response.status_code == 200:
                time_rn = get_time_rn()
                success += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
            else:
                time_rn = get_time_rn()
                failure += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
                
    while True:
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=spam, args=(channel_id, message))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
