


from core.add.plugins import *



from multiprocessing import Value

emojilist = ['😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '🙂', '🙃', '😋', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😜', '😝', '😛', '🤑', '🤗', '🤔', '🤭', '🤫', '🤥', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🙄', '😶', '😐', '😑', '😬', '🤨', '😔', '😕', '🙃', '🤢', '🤮', '🤧', '😷', '🥴', '😴', '💤', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']



def channelspammer():
    global success, failure, deleted, fdelete
    titles(title14)

    print(f"""                                   {o}[{m}01{o}] {s}>{w} Channel Spammer {o}[{m}Mentions{o}]
                                   {o}[{m}02{o}] {s}>{w} Channel Spammer {o}[{m}No Mentions{o}]
                                   {o}[{m}03{o}] {s}>{w} Ghost Pinger {o}[{m}Only Mentions{o}]""")

    print(f"                                   {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INPUT{o}] {s}>{w} ", end = ""); whichone = input()

    if whichone == "1":
        premium()
    
    elif whichone == "2":
        nomention()

    elif whichone == "3":
        premium()


def premium():
    clpr()
    print(f"                                   {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INFO{o}] {s}>{w} This is a premium feature! ")
    sleep(1)
    print(f"                                   {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INFO{o}] {s}>{w} Continuing with a free plan...")
    nomention()

def nomention():
    global success, failure, deleted, fdelete
    success = 0
    failure = 0
    deleted = 0
    fdelete = 0
    clpr()

    with open('Assets/Input/Tokens.txt') as f:
        tokens = f.read().splitlines()

    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}EMOJI AMOUNT{o}] {s}>{w} ", end = ""); PONG = input()
    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MSG AMOUNT{o}] {s}>{w} ", end = ""); MSG_AMOUNT = int(input())
    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}CHANNEL ID{o}] {s}>{w} ", end = ""); CHANNEL_ID = input()
    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MESSAGE{o}] {s}>{w} ", end = ""); MESSAGE = input()

    clpr()
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

    messages = [MESSAGE, MESSAGE]

    def send_message(token, counter):
        global success, failure, deleted, fdelete

        for message in messages:
            randomemoji = random.sample(emojilist, int(PONG))
            useemoji = " ".join([f"{em}" for em in randomemoji])
            message_with_member_id = f'```{message}``` {useemoji}'
            data = {'content': message_with_member_id}
            header = {"authorization": token}

            while counter.value < MSG_AMOUNT:
                response = requests.post(url, data=data, headers=header, json=data)
                time_rn = get_time_rn()
                counter.value += 1
                if response.status_code in [200, 201, 204]: # for vatos
                    success +=1
                    print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]")
                else:
                    try:
                        failure +=1
                        print(f"                      {o}[{m}{time_rn}{o}] {lr}[{Fore.RED}FAILURE{lr}] {o}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]") 
                    except Exception as e:
                        print(f'{e}')

                if counter.value >= MSG_AMOUNT:
                    pass

    num_threads = get_num_threads()  
    counter = Value('i', 0)  

    threads = []
    for token in tokens:
        thread = threading.Thread(target=send_message, args=(token, counter))
        thread.start()
        threads.append(thread)
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads = []

    for thread in threads:
        thread.join()
