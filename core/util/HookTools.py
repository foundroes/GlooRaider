from core.add.plugins import *


def HookSpammer():
    titles(title11)
    clearprint()
    print(f"""                                   {o}[{m}01{o}]{w} Single Webhook Spammer
                                   {o}[{m}02{o}]{w} Multi Webhook Spammer
                                   {o}[{m}03{o}]{w} Webhook Create Spammer           
    """)

    option = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if option == "1":
        global messagesuccess
        messagesuccess = 0
        clearprint()

        print(f"                                   {o}[{m}MESSAGE{o}] > {w}", end=""); message = input()
        print(f"                                   {o}[{m}AMOUNT{o}] > {w}", end=""); howmany = input()
        print(f"                                   {o}[{m}WEBHOOK{o}] > {s}[INPUT HIDDEN]{Fore.BLACK}", end=""); webhook = input()
        validate.validateWebhook(webhook)

        clearprint()
        payload = {"content": message}
        data_json = json.dumps(payload)
        headers = {"Content-Type": "application/json"}

        def send_single_webhook():
            global messagesuccess
            for i in range(int(howmany)):
                sleep(0.0001)
                time_rn = getting.get_time_rn()
                response = session.post(webhook, data=data_json, headers=headers)
                if response.status_code in [200, 204]:
                    messagesuccess += 1
                    print(f"                           {o}|{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}|{w} Message sent to the webhook {o}|{m}{response.status_code}{o}]")
                else:
                    print(f"                           {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}|{w} Failed to send the message  {o}[{m}{response.status_code}{o}]")
                    sleep(1)

        threads = []
        num_threads = getting.get_num_threads()

        for _ in range(num_threads):
            thread = threading.Thread(target=send_single_webhook)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        clearprint()
        print(f"                              {o}[{w}Webhook spammed, successfully sent the messages{o}]\n")
        input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")

    elif option == "2":

        global messagesuccess2
        messagesuccess2 = 0

        def send(webhook, message, howmany2):
            for i in range(int(howmany2)):
                global messagesuccess2
                time_rn = getting.get_time_rn()
                sleep(0.0001)
                response = session.post(webhook, data=data_json, headers=headers)
                if response.status_code in [200, 204]:
                    messagesuccess2 +=1
                    print(f"                           {o}|{w}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}|{w} Message sent to the webhook {o}|{m}{response.status_code}{o}]")
                else:
                    print(f"                           {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}|{w }Failed to send the message  {o}[{m}{response.status_code}{o}]")

        webhook_list = open(easygui.fileopenbox(), 'r').read().splitlines()
        clearprint()
        print(f"                                   {o}[{m}MESSAGE{o}] > {w}", end=""); message = input()
        print(f"                                   {o}[{m}AMOUNT{o}] > {w}", end=""); howmany2 = input()
        clearprint()
        payload = {"content": message}
        data_json = json.dumps(payload)
        headers = {"Content-Type": "application/json"}

        def run_webhook():
            while True:
                webhook = random.choice(webhook_list)
                send(webhook, message, howmany2)
                time.sleep(0.001)

        threads = []
        num_threads = getting.get_num_threads()
        for _ in range(num_threads):
            thread = threading.Thread(target=run_webhook)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        clearprint()
        print(f"                              {o}[{w}Webhooks spammed, successfully sent the messages{o}]\n")
        input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")
    elif option == "3":
        clearprint()
        print(f"                                   {o}[{m}WEBHOOK NAME{o}] > {w}", end="");                         webhook_name = input()
        print(f"                                   {o}[{m}CHANNEL ID{o}] > {w}", end="");                           channel_id = input()
        print(f"                                   {o}[{m}TOKEN{o}] > {s}[INPUT HIDDEN]{Fore.BLACK}", end="");      token = input()

        clearprint()
        output_lock = threading.Lock()
        data = {
            "name": webhook_name,
        }
        def create_webhook():
            url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
            headers = {
                "Authorization": token
            }
            reee = requests.post(url, headers=headers, json=data)
            if reee.status_code == 200:
                with output_lock:
                    time_rn = getting.get_time_rn()
                    print(f"                                 {o}|{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}|{w} Created Webhook {o}|{m}{reee.status_code}{o}]")
                    pass
            else:
                with output_lock:
                    time_rn = getting.get_time_rn()
                    clearprint()
                    print(f"                            {o}[{m}Webhooks created, reached maximum amount of webhooks{o}]\n")
                    input(f"                             {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")
        
        while True:
            create_webhook()


def HookDeleter():
    titles(title12)
    clearprint()
    
    print(f"                                   {o}[{m}WEBHOOK{o}] > {s}[INPUT HIDDEN]{Fore.BLACK}", end=""); wbh = input()
    validate.validateWebhook(wbh)
    clearprint()
    
    x = requests.delete(wbh)
    if x.status_code == 404:
        print(f"                                  {o}[{m}Failed to deleted the requested webhook{o}]")
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")
    else:
        print(f"                                 {o}[{m}Successfully deleted the requested webhook{o}]")
        input(f"\n                                  {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")


def HookLookup():
    clear()
    titles(title13)
    print(toolprint)
    webhook_url = input(f'                                   {o}[{m}GLOO{o}] {s}| {o}[{m}WEBHOOK{o}] {s}> [INPUT HIDDEN]{Fore.BLACK}')
    validate.validateWebhook(webhook_url)


    wbhk = Webhook(webhook_url)
    xxxx = requests.get(wbhk.url)

    if xxxx.status_code == 404:
        clearprint()
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Webhook doesn't exist!")
        sleep(1)
        input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")
    if xxxx.status_code == 402:
        clearprint()
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Webhook doesn't exist!")
        sleep(1)
        input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")
    else:
        wbhk.get_info()
        clearprint()
        
        print(f'                                   {o}[{m}WEBHOOK NAME{o}]{w} {wbhk.default_name}\n')

        print(f'                                   {o}[{m}WEBHOOK ID{o}]{w} {wbhk.id}')
        print(f'                                   {o}[{m}CHANNEL ID{o}]{w} {wbhk.channel_id}')
        print(f'                                   {o}[{m}GUILD ID{o}]{w} {wbhk.guild_id}')

        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}")