from core import *

def BioChanger():
    titles('BIO')
    clearprint()
    global success, failure
    success = 0
    failure = 0

    bio = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}BIO{o}] {s}>{w} ")

    clearprint()

    if bio == "" or bio is None:
        bio = "https://gloo.lol"
    else:
        bio = bio

    def bio_changer(token):
        global success, failure
        payload = {
            "bio": bio
        }

        sesheaders = headers.copy()
        sesheaders.update({'Authorization': token})

        response = requests.patch("https://discord.com/api/v9/users/@me/profile", headers=sesheaders, json=payload)
        with lock:
            time_rn = getting.get_time_rn()
            if response.status_code in [200, 202]:
                success += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
            else:
                failure += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")


    tokens = getting.get_tokens()
    num_threads = getting.get_num_threads()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(bio_changer, tokens)

    clear()
    print(toolprint)

    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clearprint()
        print(f"""                            {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Changed bio of the token.
                            {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Failed to change bio of the token.""")
        input(f"\n                            {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")
    
    elif choose == "":
        pass
