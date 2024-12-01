


from core import *

def ChannelSpammer():
    global success, failure
    clearprint()
    titles('CHANNEL')

    print(f"""                                     {o}[{m}01{o}] {s}>{w} Channel Spammer {o}[{m}Mentions{o}]
                                     {o}[{m}02{o}] {s}>{w} Channel Spammer {o}[{m}No Mentions{o}]""")

    whichone = input(f"\n                                     {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INPUT{o}] {s}>{w} ")

    if whichone == "1":
        Premium()
        NoMentionSpam()
    
    elif whichone == "2":
        NoMentionSpam()

            
def NoMentionSpam():
    global success, failure

    success = 0
    failure = 0

    def stop_listener():
        keyboard.wait('x')
        stop_event.set()

    stop_event = threading.Event()
    stop_thread = threading.Thread(target=stop_listener, daemon=True)
    stop_thread.start()

    clearprint()
    titles('CHANNEL')

    tokens = getting.get_tokens()

    PONG = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}EMOJI AMOUNT{o}] {s}>{w} ")

    pong_number = int(PONG)
    if pong_number >= 70:
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Maximum amount is 69!")
        sleep(0.7)
        NoMentionSpam()

    CHANNEL_ID = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}CHANNEL ID{o}] {s}>{w} ")
    MESSAGE = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MESSAGE{o}] {s}>{w} ")

    
    if not (PONG and CHANNEL_ID and MESSAGE):
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return

    clearprint()
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

    def send_message(token):
        global success, failure

        while not stop_event.is_set():
            ezem = random.sample(emojilist, int(PONG))
            emmen = " ".join([f"{em}" for em in ezem])
            message_with_emojies = f'{emmen} ```{MESSAGE}```'
            data = {'content': message_with_emojies}

            sesheaders = headers.copy()
            sesheaders.update({"Authorization": token})

            try:
                response = requests.post(url, json=data, headers=sesheaders)
                time_rn = getting.get_time_rn()
                if response.status_code in [200, 201, 204]:
                    success += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
                else:
                    failure += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
            except Exception as e:
                failure += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}ERROR{lr}]   {s}| {w}{token[:37]} {o}[{m}{e}{o}]")

            sleep(1)  

    num_threads = getting.get_num_threads() 
    threads = []

    for token in tokens:
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

        thread = threading.Thread(target=send_message, args=(token,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    clearprint()
    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clearprint()
        print(f"""                            {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:04}{o}] {s}>{w} Sent the messages to the channel.
                            {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:04}{o}] {s}>{w} Failed to send the messages.\n""")

        input(f"                            {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")
