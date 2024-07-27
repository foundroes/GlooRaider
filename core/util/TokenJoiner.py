import              string
import              os
import              random
import              ctypes

from core.add import dtypes
from core.add.plugins import *

import concurrent.futures
import tls_client

def tokenjoiner():
        clearprint()
        titles(title5)
        with open('assets/input/tokens.txt', 'r') as file:
            tokens = [line.strip() for line in file]


        max_threads = int(config.get('MAIN', 'threads'))

        instances = []
        invite = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INVITE{o}] {s}>{w} discord.gg/")
        clearprint()
        for i in range(len(tokens)):
            header = dtypes.OtherInfo.headers
            instances.append(dtypes.Instance(
                client=tls_client.Session(
                client_identifier=f"chrome_{random.randint(110,115)}",
                random_tls_extension_order=True
            ),
                token=tokens[i],
                headers=header,
                invite=invite
            ))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = [executor.submit(intilize.start, i) for i in instances]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"                      {o}[{m}##:##:##{o}] {lr}[{r}ERROR{lr}]   {s}|{w} {e}")

        clearprint()
        input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")

class Joiner:
    def __init__(self, data:dtypes.Instance) -> None:
        self.session=data.client
        self.session.headers = data.headers
        self.get_cookies()
        self.instance = data
    def rand_str(self, length:int) -> str:
        return ''.join(random.sample(string.ascii_lowercase+string.digits,length))
    def get_cookies(self) -> None:
        site=self.session.get("https://discord.com")
        self.session.cookies=site.cookies

    def join(self) -> None:
            self.session.headers.update({"Authorization":self.instance.token})
            result=self.session.post(f"https://discord.com/api/v9/invites/{self.instance.invite}",json={
                'session_id': self.rand_str(32),
            })
            if result.status_code==200:
                time_rn = getting.get_time_rn()
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {self.instance.token[:37]} {o}[{m}{result.status_code}{o}]")
            else:
                time_rn = getting.get_time_rn()
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}|{w} {self.instance.token[:37]} {o}[{m}{result.status_code}{o}]")
                
class logger: # TOKEN JOINER
    colors_table = dtypes.OtherInfo.colortable
    def convert(color):
        if not color.__contains__("#"):
            return logger.colors_table[color]
        else:
            return color
class intilize:
        def start(i):
            Joiner(i).join()