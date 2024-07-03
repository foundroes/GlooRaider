
from core.add.plugins import *







def onliner(): # TOKEN ONLINER WORKS
    titles(title3)
    clpr()
    print(f'                              {o}[{w}Choose status: {o}"{m}online{o}"{w}, {o}"{m}dnd{o}"{w}, {o}"{m}idle{o}"{w}, {o}"{m}random{o}"]\n')
    choice = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")
    if choice in ["1", "online"]:
        status = "online"
    elif choice in ["2", "dnd"]:
        status = "dnd"
    elif choice in ["3", "idle"]:
        status = "idle"
    elif choice in ["4", "random"]:
        status_list = ["online", "idle", "dnd"]
        status = random.choice(status_list)
    else:
        status_list = ["online", "idle", "dnd"]
        status = random.choice(status_list)

    clpr()
    details = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}DETAILS{o}] {s}>{w} ")
    state = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}STATE{o}] {s}>{w} ")
    name = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}NAME{o}] {s}>{w} ")
    platform = sys.platform

    lock = threading.Lock()
    clpr()

    def tokenonliner(token):
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

        with lock:
            time_rn = get_time_rn()
            print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}+++{o}]")
            pass

    def main():
        with open("Assets/Input/Tokens.txt", "r", encoding='utf-8') as f:
            tokens = f.read().splitlines()

        num_threads = get_num_threads()

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            executor.map(tokenonliner, tokens)

    main()
    clpr()
    print(f'                               {o}[{w}Tokens are active and will stay for some time{o}]')
    input(f"\n                                {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")