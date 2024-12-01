
from core import *

def Onliner(): # TOKEN ONLINER WORKS
    clearprint()
    titles('ONLINER')
    print(f'                             {o}[{w}Choose a status: {o}"{m}online{o}"{w}, {o}"{m}dnd{o}"{w}, {o}"{m}idle{o}"{w}, {o}"{m}random{o}"]\n')

    status_choice = input(f"                              {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if status_choice in ["1", "online"]:
        status = "online"
    elif status_choice in ["2", "dnd"]:
        status = "dnd"
    elif status_choice in ["3", "idle"]:
        status = "idle"
    elif status_choice in ["4", "random"]:
        status_list = ["online", "idle", "dnd"]
        status = random.choice(status_list)
    else:
        status_list = ["online", "idle", "dnd"]
        status = random.choice(status_list)

    clearprint()

    details = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}DETAILS{o}] {s}>{w} ")
    state = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}STATE{o}] {s}>{w} ")
    name = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}NAME{o}] {s}>{w} ")
    platform = sys.platform
    output_lock = threading.Lock()

    clearprint()

    def token_onliner(token):
        ws_online = websocket.WebSocket()
        ws_online.connect("wss://gateway.discord.gg/?encoding=json&v=9")
        response = ws_online.recv()
        event = json.loads(response)
        ws_online.send(json.dumps({
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": platform,
                    "$browser": "RTB",
                    "$device": f"{platform} Device",
                },
                "presence": {
                "game": {
                    "name": name,
                    "type": 0,
                    "details": details,
                    "state": state,
                },
                "status": status,
                "since": 0,
                "activities": [],
                "afk": False,
                },
            },
            "s": None,
            "t": None
        }))

        with output_lock:
            time_rn = getting.get_time_rn()
            print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}+++{o}]")
            pass

    tokens = getting.get_tokens()

    num_threads = getting.get_num_threads()  # Getting number of threads from config.ini

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(token_onliner, tokens)
            
    clearprint()
    
    print(f'                               {o}[{w}Tokens are active and will stay for some time{o}]')
    input(f"\n                                {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")