from core.add.plugins import *



def leaver():
    titles(title4)
    clpr()
    ID = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}GUILD ID{o}] {s}>{w} ")
    clpr()

    apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

    token = get_tokens()
    threads = []

    with open('Assets/Input/Tokens.txt', 'r') as handle:
        tokens = handle.readlines()
        for i in tokens:
            token = i.rstrip()
            headers = {
                'Authorization': token,
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            time_rn = get_time_rn()
            print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}+++{o}]")

            num_threads = get_num_threads()

            t = threading.Thread(target=requests.delete, args=(apilink,), kwargs={'headers': headers})
            threads.append(t)
            t.start()
            
            if len(threads) >= num_threads:
                for t in threads:
                    t.join()
                threads = []

    for t in threads:
        t.join()
    clpr()
    print(f'                             {o}[{w}Tokens left the server, try again if some did not{o}]')
    input(f"\n                              {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")