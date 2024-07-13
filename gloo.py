


from pystyle import System

from core.add.plugins       import *
from core.add.imports       import *
from core.add.common        import *


System.Size(110, 20)

def gloopage():
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'[Gloo Raider]  |  [OPEN-SOURCE]  |  [Tokens: {counttokens}]  |  [Proxies: {countproxies}]  |  [https://gloo.lol]')
        clear()
        print(toolprint)
        print(mainpage)


        def handle_choice(choice):
            actions = {
                '1': formater,
                '2': tokenchecker,
                '3': onliner,
                '4': leaver,
                '5': TokenInfo,
                '6': removeduplicates,
                '7': pronounceChanger,
                '8': statusrotater,
                '9': namechanger,
                '10': biochanger,
                '11': HookSpammer,
                '12': HookDeleter,
                '13': HookLookup,
                '14': channelspammer,
                '15': BasicSpammer,
                '16': soundboard,
                '17': auditspammer,
                '17': website,
                '17': discord,
                '20': sys.exit,
            }

            if choice in actions:
                if choice in ['1', '11', '12', '13']:
                    actions[choice]()
                elif os.path.exists(dirchecker):
                    if os.path.getsize(dirchecker) == 0:
                        validate.checkfortokens()
                    else:
                        clearprint()
                        actions[choice]()
                gloopage()


        choice = input(f"       {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")
        handle_choice(choice)


gloopage()