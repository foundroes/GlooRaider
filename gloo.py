
import asyncio
import sys
import os
import webbrowser

from pystyle import System

from core.add.plugins       import *
from core.add.imports       import *
from core.add.common        import *


System.Size(110, 20)


def checkfortokens():
        clpr()
        print(f"                                 {o}[{w}No tokens found in {dirchecker}{o}]")
        input(f"\n                                  {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()

def validateWebhook(hook):
    if not "api/webhooks" in hook:
        clpr()
        print(f"\n                                  {o}[{w}Invalid webhook, failed to run the tool{o}]")
        sleep(2)
        gloopage()

def validatetoken(token):
    response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "de-DE"})
    if response.status_code == 200:
        pass
    else:
        clpr()
        print(f"                                  {o}[{w}Your token is invalid, please try again{o}]")
        sleep(2)
        gloopage()


def gloopage():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [OPEN-SOURCE]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')
        clear()
        print(mainprint)
        print(mainpage)
        choice = input(f"       {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

        if choice == '1': 
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    formater()

        elif choice == '2': 
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    tokenchecker()

        elif choice == '3':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    onliner()

        elif choice == '4':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    leaver()

        elif choice == '5':
            clpr()
            token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}>{Fore.LIGHTBLACK_EX} [INPUT HIDDEN]{Fore.BLACK}")
            clear()
            validatetoken(token)
            TokenInfo(token)

        elif choice == '6':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    removeduplicates()
                    input(f"\n                          {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()

        elif choice == '7':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    pronounceChanger()

        elif choice == '8':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    statusrotater()

        elif choice == '9': 
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    namechanger()

        elif choice == '10':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    biochanger()

        elif choice == '11':
            titles(title11)
            clpr()
            print(f"""                                   {o}[{m}01{o}]{w} Single Webhook Spammer
                                   {o}[{m}02{o}]{w} Multi Webhook Spammer
                                   {o}[{m}03{o}]{w} Webhook Create Spammer           
    """)

            option = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

            if option == "1":
                global messagesuccess
                messagesuccess = 0
                clpr()

                print(f"                                   {o}[{m}MESSAGE{o}] > {w}", end=""); message = input()
                print(f"                                   {o}[{m}AMOUNT{o}] > {w}", end=""); howmany = input()
                print(f"                                   {o}[{m}WEBHOOK{o}] > {s}[INPUT HIDDEN]{Fore.BLACK}", end=""); webhook = input()
                validateWebhook(webhook)

                clpr()
                payload = {"content": message}
                data_json = json.dumps(payload)
                headers = {"Content-Type": "application/json"}

                def send_single_webhook():
                    global messagesuccess
                    for i in range(int(howmany)):
                        sleep(0.0001)
                        time_rn = get_time_rn()
                        response = session.post(webhook, data=data_json, headers=headers)
                        if response.status_code in [200, 204]:
                            messagesuccess += 1
                            print(f"                           {o}|{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}|{w} Message sent to the webhook {o}|{m}{response.status_code}{o}]")
                        else:
                            print(f"                           {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}|{w} Failed to send the message  {o}[{m}{response.status_code}{o}]")
                            sleep(1)

                threads = []
                num_threads = get_num_threads()

                for _ in range(num_threads):
                    thread = threading.Thread(target=send_single_webhook)
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

                clpr()
                print(f"                              {o}[{w}Webhook spammed, successfully sent the messages{o}]\n")
                input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()

            elif option == "2":

                global messagesuccess2
                messagesuccess2 = 0

                def send(webhook, message, howmany2):
                    for i in range(int(howmany2)):
                        global messagesuccess2
                        time_rn = get_time_rn()
                        sleep(0.0001)
                        response = session.post(webhook, data=data_json, headers=headers)
                        if response.status_code in [200, 204]:
                            messagesuccess2 +=1
                            print(f"                           {o}|{w}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}|{w} Message sent to the webhook {o}|{m}{response.status_code}{o}]")
                        else:
                            print(f"                           {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {o}|{w }Failed to send the message  {o}[{m}{response.status_code}{o}]")

                webhook_list = open(easygui.fileopenbox(), 'r').read().splitlines()
                clpr()
                print(f"                                   {o}[{m}MESSAGE{o}] > {w}", end=""); message = input()
                print(f"                                   {o}[{m}AMOUNT{o}] > {w}", end=""); howmany2 = input()
                clpr()
                payload = {"content": message}
                data_json = json.dumps(payload)
                headers = {"Content-Type": "application/json"}

                def run_webhook():
                    while True:
                        webhook = random.choice(webhook_list)
                        send(webhook, message, howmany2)
                        time.sleep(0.001)

                threads = []
                num_threads = get_num_threads()
                for _ in range(num_threads):
                    thread = threading.Thread(target=run_webhook)
                    thread.start()
                    threads.append(thread)

                for thread in threads:
                    thread.join()

                clpr()
                print(f"                              {o}[{w}Webhooks spammed, successfully sent the messages{o}]\n")
                input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()

            elif option == "3":
                clpr()
                print(f"                                   {o}[{m}WEBHOOK NAME{o}] > {w}", end="");                         webhook_name = input()
                print(f"                                   {o}[{m}CHANNEL ID{o}] > {w}", end="");                           channel_id = input()
                print(f"                                   {o}[{m}TOKEN{o}] > {s}[INPUT HIDDEN]{Fore.BLACK}", end="");      token = input()

                clpr()
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
                            time_rn = get_time_rn()
                            print(f"                                 {o}|{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {o}|{w} Created Webhook {o}|{m}{reee.status_code}{o}]")
                            pass
                    else:
                        with output_lock:
                            time_rn = get_time_rn()
                            clpr()
                            print(f"                            {o}[{m}Webhooks created, reached maximum amount of webhooks{o}]\n")
                            input(f"                             {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()
                
                while True:
                    create_webhook()

        elif choice == '12':
            titles(title12)
            clpr()
            
            print(f"                                   {o}[{m}WEBHOOK{o}] > {s}[INPUT HIDDEN]{Fore.BLACK}", end=""); wbh = input()
            validateWebhook(wbh)
            clpr()
            
            x = requests.delete(wbh)
            if x.status_code == 404:
                print(f"                                  {o}[{m}Failed to deleted the requested webhook{o}]")
                input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()
            else:
                print(f"                                 {o}[{m}Successfully deleted the requested webhook{o}]")
                input(f"\n                                  {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()

        elif choice == '13': 
            clear()
            titles(title13)
            print(toolprint)
            webhook_url = input(f'                                   {o}[{m}GLOO{o}] {s}| {o}[{m}WEBHOOK{o}] {s}> [INPUT HIDDEN]{Fore.BLACK}')
            validateWebhook(webhook_url)


            wbhk = Webhook(webhook_url)
            xxxx = requests.get(wbhk.url)

            if xxxx.status_code == 404:
                clpr()
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Webhook doesn't exist!")
                sleep(1)
                input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()
            if xxxx.status_code == 402:
                clpr()
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Webhook doesn't exist!")
                sleep(1)
                input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()
            else:
                wbhk.get_info()
                clpr()
                
                print(f'                                   {o}[{m}WEBHOOK NAME{o}]{w} {wbhk.default_name}\n')

                print(f'                                   {o}[{m}WEBHOOK ID{o}]{w} {wbhk.id}')
                print(f'                                   {o}[{m}CHANNEL ID{o}]{w} {wbhk.channel_id}')
                print(f'                                   {o}[{m}GUILD ID{o}]{w} {wbhk.guild_id}')

                input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.{Fore.BLACK}"); gloopage()

        elif choice == '14':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    channelspammer()
                    from core.util.ChannelSpammer import success, failure, deleted, fdelete
                    clpr()
                        
                    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
                    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

                    if choose == "show":
                        clpr()
                        print(f"""                            {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:04}{o}] {s}>{w} Sent the messages to the channel.
                            {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:04}{o}] {s}>{w} Failed to send the messages.""")                 
                        input(f"                            {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back."); gloopage()

        elif choice == '15':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    BasicSpammer()
                    clpr()
                    print(f'                              {o}[{m}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
                    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

                    if choose == "show":
                        clpr()
                        print(f"""                            {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:04}{o}] {s}>{w} Sent the messages to the channel.
                            {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:04}{o}] {s}>{w} Failed to send the messages.\n""")
                        input(f"                            {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back."); 

                    elif choose == "":
                        pass

        elif choice == '16':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    soundboard()

        elif choice == '17':
            if os.path.exists(dirchecker):
                if os.path.getsize(dirchecker) == 0:
                    checkfortokens()
                else:
                    clpr()
                    auditspammer()

        elif choice == '18':
            discord = "https://discord.gg/uJE9rfJ7Tz"
            webbrowser.open(discord)

        elif choice == '19':
            website = "https://lostroes.sell.app"
            webbrowser.open(website)

        elif choice == '20':
            sys.exit()

        else:
            gloopage()
gloopage()