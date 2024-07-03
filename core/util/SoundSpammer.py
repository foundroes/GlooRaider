
from core.add.plugins import *

import concurrent.futures
import threading
import ctypes
import time
import random

def soundboard():
    clpr()
    titles(title16)

    server_id = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}SERVER ID{o}] {s}>{w} ")
    channel_id = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}CHANNEL ID{o}] {s}>{w} ")
    amount = int(input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}AMOUNT{o}] {s}>{w} "))
    clpr()

    output_lock = threading.Lock()
    defean_voice = False
    mute_voice = False
    stream_voice = True
    video_voice = True

    # Function to handle voice joining and sound playing
    def voice_joiner(token, amount):
        for _ in range(amount):
            ws_voice = WebSocket()
            ws_voice.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            ws_voice.send(dumps(
                {
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "windows",
                            "$browser": "Discord",
                            "$device": "desktop"
                        }
                    }
                }))
            ws_voice.send(dumps({
                "op": 4,
                "d": {
                    "guild_id": server_id,
                    "channel_id": channel_id,
                    "self_mute": mute_voice,
                    "self_deaf": defean_voice, 
                    "self_stream?": stream_voice, 
                    "self_video": video_voice
                }
            }))
            ws_voice.send(dumps({
                "op": 18,
                "d": {
                    "type": "guild",
                    "guild_id": server_id,
                    "channel_id": channel_id,
                    "preferred_region": "spain"
                }
            }))
            ws_voice.send(dumps({
                "op": 1,
                "d": None
            }))
            time.sleep(0.5)
            numbers = random.randint(1, 6)
            if numbers == 1:
                emoji = "🦆"
            elif numbers == 2:
                emoji = "🔊"
            elif numbers == 3:
                emoji = "🦗"
            elif numbers == 4:
                emoji = "👏"
            elif numbers == 5:
                emoji = "🎺"
            elif numbers == 6:
                emoji = "🥁"
            else:
                emoji = "🦆"
                
            payload = {
                "emoji_id": None,
                "emoji_name": emoji,
                "sound_id": numbers
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

            response = session.post(f"https://discord.com/api/v9/channels/{channel_id}/voice-channel-effects", headers=headers, json=payload)
            if response.status_code == 204:
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"                      {o}[{m}{time_rn}{o}] {lb}[{b}PLAYING{lb}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
            else: 
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
            time.sleep(1.5)
            ws_voice.close()
            time.sleep(1.5)

    def process_token(token, amount):
        voice_joiner(token, amount)

    clpr()
    with open("Assets/Input/Tokens.txt", "r", encoding='utf-8') as f:
        tokens = f.read().splitlines()
        for token in tokens:
            with output_lock:
                time_rn = get_time_rn()
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}| {w}{token[:37]} {o}[{m}+++{o}]")
                pass
    # Reading number of threads from config.ini
    num_threads = get_num_threads()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for token in tokens:
            executor.submit(process_token, token, amount)