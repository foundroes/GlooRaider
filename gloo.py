


from core import *
from core.util import *


System.Size(110, 20)
BackgroundRPC()

webbrowser.open('https://discord.gg/pqaYpfXDHj')

class UI:
    def page1():
        while True:
            titles('PAGE1')
            clearprint()
            print(page1menu)

            def handler(option):
                actions = {
                    '1':  Formatter,
                    '2':  Premium,
                    '3':  Checker,
                    '4':  Onliner,
                    '5':  Premium,
                    '6':  PronChanger,
                    '7':  TokenJoiner,
                    '8':  GuildLeaver,
                    '9':  NameChanger,
                    '10': BioChanger,
                    '11': RemoveDupes,
                    '12': Premium,
                    '13': ChannelSpammer,
                    '14': GroupSpammer,
                    '15': ReplySpammer,
                    '16': Nuker,
                    '17': Login,
                    '18': Info,
                    '19': GuildInfo,
                    '20': Socials

                }

                if option in actions:
                    if os.path.exists(checktokens):
                        if os.path.getsize(checktokens) == 0 and option in addons.tokenoptions:
                            addons.checkfortokens(option)
                        else:
                            clearprint()
                            actions[option]()

            option = input(f"     {o}[{m}GLOO{o}]{m} {s}| {o}[{m}INPUT{o}]{m} {s}>{w} ")
            handler(option)

UI.page1()

