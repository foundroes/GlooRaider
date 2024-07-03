
from core.add.plugins import *


def auditspammer():
    global success, failure
    success = 0
    failure = 0
    titles(title17)
    clpr()
    lock = threading.Lock()
    server_id = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}SERVER ID{o}] {s}>{w} ")
    amount = int(input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}AMOUNT{o}] {s}>{w} "))
    clpr()

    def spamlogs(token, server_id, amount):
        global success, failure
        payload = {
            "nick": random.choice(nicknames)
        }

        headers = {
            'authorization': token,
            "accept": "*/*",
            "accept-language": "en-GB",
            "content-length": str(len(json.dumps(payload))),
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

        for _ in range(amount):
            response = session.patch(f"https://discord.com/api/v9/guilds/{server_id}/members/@me/nick", headers=headers, json=payload)
            if response.status_code != 200:

                with lock:
                    time_rn = get_time_rn()
                    failure += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")  
                    time.sleep(0.10)
            else:
                with lock:
                    time_rn = get_time_rn()
                    success += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
                    time.sleep(0.10)
                

    tokens = get_tokens()
    
    threads = []

    num_threads = get_num_threads()
    
    for token in tokens:
        for _ in range(num_threads):
            t = threading.Thread(target=spamlogs, args=(token, server_id, amount))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    clpr()
        
    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clpr()
        print(f"""                            {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Bot{o}/{w}Audit logs spammed by tokens.
                            {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Failed to spam the Bot{o}/{w}Audit logs.\n""")
        input(f"                            {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")
        
    elif choose == "":
        pass