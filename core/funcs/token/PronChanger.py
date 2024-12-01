from core import *

def PronChanger():
    titles('PRON')

    global success, failure
    success = 0
    failure = 0

    pronouns = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}PRONOUNS{o}] {s}>{w} ")

    clearprint()
    if not pronouns:
        pronouns = "https://gloo.lol"

    def pronoun_changer(token):
        global success, failure
        payload = {
            "pronouns": pronouns
        }

        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})
        session = Client.get_session()

        response = session.patch(f"https://discord.com/api/v9/users/@me/profile", headers=sesheaders, json=payload)
        time_rn = getting.get_time_rn()
        if response.status_code == 200:
            success += 1
            print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]{d}")
        else:
            failure += 1
            print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}|{w} {token[:37]} {o}[{m}{response.status_code}{o}]{d}")

    tokens = getting.get_tokens()

    num_threads = getting.get_num_threads()  # Getting number of threads from config.ini

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(pronoun_changer, tokens)
    
    clearprint()

    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clearprint()
        print(f"""                       {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Changed the pron. of the token in the server!
                       {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Failed to change the pron. of the token!""")
        input(f"\n                       {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")
    
    elif choose == "":
        pass
