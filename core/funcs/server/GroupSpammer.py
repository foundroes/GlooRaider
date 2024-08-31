



from core import *

def GroupSpammer():
    clearprint()
    titles('CHANNEL')

    print(f"""                                     {o}[{m}01{o}] {s}>{w} Group Spammer {o}[{m}With Members{o}]
                                     {o}[{m}02{o}] {s}>{w} Group Spammer {o}[{m}Only Token{o}]""")

    whichone = input(f"\n                                     {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INPUT{o}] {s}>{w} ")

    if whichone == "1":
        Premium()
        NoAddingMembers()

    elif whichone == "2":
        NoAddingMembers()


def NoAddingMembers():
    global success, failure, limited
    success = 0
    failure = 0
    limited = 0
    titles('GROUP')
    def create_group(token, groupname, output_lock):
        global success, failure, limited

        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})
        session = tls_client.Session(
            client_identifier="chrome_116",
        )

        try:
            response_recipients = session.post('https://discord.com/api/v9/users/@me/channels', headers=sesheaders, json={
                    "recipients": []
            })
            newjson = json.loads(response_recipients.content)
            id = newjson['id']
            sleep(0.2)
            payload = {
                'name': groupname
            }
            response = session.patch(f'https://discord.com/api/v9/channels/{id}', headers=sesheaders, json=payload)
            if response.status_code == 200:
                with output_lock:
                    success +=1
                    time_rn = getting.get_time_rn()
                    print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]{d}")
            else:
                with output_lock:
                    failure +=1
                    time_rn = getting.get_time_rn()
                    print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]{d}")
        except:
            with output_lock:
                time_rn = getting.get_time_rn()
                print(f"                      {o}[{m}{time_rn}{o}] {ly}[{y}LIMITED{ly}]{y} {s}| {w}{token[:37]} {o}[{m}xxx{o}]{d}")
                limited +=1


    groupname = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}GROUP NAME{o}] {s}>{w} ")
    howmany = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}AMOUNT{o}] {s}>{w} ")
    token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")

    if not addons.validatetoken(token):
        return  

    if not (groupname and howmany):
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return
    
    clearprint()
    output_lock = threading.Lock()
    threads = []
    num_threads = getting.get_num_threads()  # Getting number of threads from config.ini

    for i in range(int(howmany)):
        thread = threading.Thread(target=create_group, args=(token, groupname, output_lock))
        threads.append(thread)
        thread.start()

        # Limit number of concurrent threads
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    for thread in threads:
        thread.join()

    clearprint()
        
    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")
    
    if choose == "show":
        clearprint()
        print(f"""                             {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Groups created on users account.
                             {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Groups could not be created.
                             {ly}[{y}LIMITED{ly}]{y} {s}| {o}[{m}{limited:03}{o}] {s}>{w} Token is rate-limited.\n""")
        input(f"                             {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")
        
    elif choose == "":
        pass