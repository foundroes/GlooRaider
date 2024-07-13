

from core.add.plugins import *


def TokenInfo():

    token = input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{Fore.BLACK}")
    titles(title5)
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getting.get_headers(token))

    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    mfa = r.json()['mfa_enabled']
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getting.get_headers(token))
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)

    if has_nitro:
        from datetime import datetime
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)
        
    print(f"""                                   {o}[{m}MAIL{o}]{w} {email}
                                   {o}[{m}PHONE{o}]{w} {phone}
                                   {o}[{m}2FA{o}]{w} {mfa}

                                   {o}[{m}USER ID{o}]{w} {userID}
                                   {o}[{m}USER{o}]{w} {userName}
                                   {o}[{m}NITRO{o}]{w} {has_nitro} / {days_left if has_nitro else "0"} days""")
    billingcheck = input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}BILLING{o}] {w}y/n {s}>{w} ")

    if billingcheck in yeslist:
        clearprint()
        print(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} This is a premium feature!")
        sleep(2)
        pass
        
