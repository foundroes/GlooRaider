from core import *

def GuildLeaver():
    titles('TGleaver')
    clearprint()

    ID = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}GUILD ID{o}] {s}>{w} ")

    if not ID:
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return
    
    clearprint()

    apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)
    threads = []
    tokens = getting.get_tokens()  

    for token in tokens:
        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token.strip()})

        time_rn = getting.get_time_rn()
        print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}+++{o}]")

        num_threads = getting.get_num_threads()

        t = threading.Thread(target=requests.delete, args=(apilink,), kwargs={'headers': sesheaders})
        threads.append(t)
        t.start()
        
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

    clearprint()
    print(f'                             {o}[{w}Tokens left the server, try again if some did not{o}]')
    input(f"\n                              {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")

