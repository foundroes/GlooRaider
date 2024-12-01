import re
import time
import uuid
import json
import httpx
import base64
import random
import requests
import tls_client

from random import randint
from time import sleep
from core import clearprint, o, m,  w, s

class WIN_headers:
    def __init__(self):
        clearprint()
        st = time.time()
        print(f"                                {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INFO{o}] {s}>{w} Getting Discord Desktop Info\n"); sleep(0.5)
        clearprint()
        self.native_builds = self.native_build()
        self.main_versions = self.main_version()
        self.client_builds = self.client_build()
        self.chrome = WIN_headers.chrome_version()
        self.electron = "22.3.26"
        self.safari = "537.36"
        self.os_version = "10.0.19045"
        self.user_agent = f"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/{self.safari} (KHTML, like Gecko) discord/{self.main_versions} Chrome/{self.chrome} Electron/{self.electron} Safari/{self.safari}"
        rn = str(time.time() - st)
        
        print(f"                      {o}[{m}GLOO{o}] {s}|{w} {o}[{m}USER AGENT{o}] {s}--->{w} {self.user_agent[:36]}...")
        print(f"                      {o}[{m}GLOO{o}] {s}|{w} {o}[{m}BUILD NUM{o}] {s}---->{w} {self.client_builds}")
        print(f"                      {o}[{m}GLOO{o}] {s}|{w} {o}[{m}NATIVE BUILD{o}] {s}->{w} {self.native_builds}")
        print(f"                      {o}[{m}GLOO{o}] {s}|{w} {o}[{m}APP VER{o}] {s}------>{w} {self.main_versions}")

        print(f"\n                      {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INFO{o}] {s}>{w} Successfully Built Headers in {rn[:5]} Seconds"); sleep(1)

        self.x_super_properties = self.desktop_xprops()
        self.dict = self.returner()

    @staticmethod
    def chrome_version() -> str:
        try:
            r = requests.get("https://versionhistory.googleapis.com/v1/chrome/platforms/linux/channels/stable/versions")
            data = json.loads(r.text)
            return data['versions'][0]['version']
        except Exception:
            return "108.0.5359.215"

    def desktop_xprops(self):
        return base64.b64encode(json.dumps({
            "os":"Windows",
            "browser":"Discord Client",
            "release_channel":"stable",
            "client_version":self.main_versions,
            "os_version":self.os_version,
            "os_arch":"x64",
            "app_arch":"ia32",
            "system_locale":"en",
            "browser_user_agent":self.user_agent,
            "browser_version":self.electron,
            "client_build_number":self.client_builds,
            "native_build_number":self.native_builds,
            "client_event_source":None,
            "design_id":0
        }).encode()).decode()
    
    def native_build(self) -> int:
        return int(requests.get(
            "https://updates.discord.com/distributions/app/manifests/latest",
            params = {
                "install_id":'0',
                "channel":"stable",
                "platform":"win",
                "arch":"x86"
            },
            headers = {
                "user-agent": "Discord-Updater/1",
                "accept-encoding": "gzip"
        }).json()["metadata_version"])

    def client_build(self) -> int:
        page = requests.get("https://discord.com/app").text.split("app-mount")[1]
        assets = re.findall(r'src="/assets/([^"]+)"', page)[::-1]

        for asset in assets:
            js = requests.get(f"https://discord.com/assets/{asset}").text
            
            if "buildNumber:" in js:
                return int(js.split('buildNumber:"')[1].split('"')[0])

    def main_version(self) -> str:
        app = requests.get(
            "https://discord.com/api/downloads/distributions/app/installers/latest",
            params = {
                "channel":"stable",
                "platform":"win",
                "arch":"x86"
            },
            allow_redirects = False
        ).text

        return re.search(r'x86/(.*?)/', app).group(1)
    
    def returner(self):
        return {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en,en-US;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.user_agent,
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Europe/Stockholm',
            'x-super-properties': self.x_super_properties
        }

    def __call__(self):
        return self.dict

def get_headers():
    return WIN_headers()()

headers = get_headers()

class Client:
    @staticmethod
    def get_session(token: str = "", cookie: bool = True):
        ident = {
            "Windows": f"chrome_{WIN_headers.chrome_version()[:3]}"
        }["Windows"]  

        session = tls_client.Session(
            client_identifier=ident,
            random_tls_extension_order=True
        )
        
        session.headers = headers
        if token:
            session.headers.update({"Authorization": token})
        if cookie:
            site = session.get("https://discord.com")
            session.cookies = site.cookies

        return session

