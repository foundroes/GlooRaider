from core import *


def Info():
    titles('TINFO')
    token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")
    
    if not addons.validatetoken(token):
        return  

    if not (token):
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return

    sesheaders = headers.copy()
    sesheaders.update({"Authorization": token.strip()})

    try:
        r = requests.get('https://discord.com/api/v9/users/@me', headers=sesheaders)

        badges = ""
        Discord_Employee = 1
        Partnered_Server_Owner = 2
        HypeSquad_Events = 4
        Bug_Hunter_Level_1 = 8
        House_Bravery = 64
        House_Brilliance = 128
        House_Balance = 256
        Early_Supporter = 512
        Bug_Hunter_Level_2 = 16384
        Early_Verified_Bot_Developer = 131072

        flags = r.json()['flags']
        if (flags == Discord_Employee):
            badges += "Staff, "
        if (flags == Partnered_Server_Owner):
            badges += "Partner, "
        if (flags == HypeSquad_Events):
            badges += "Hypesquad Event, "
        if (flags == Bug_Hunter_Level_1):
            badges += "Green Bughunter, "
        if (flags == House_Bravery):
            badges += "Bravery, "
        if (flags == House_Brilliance):
            badges += "Brillance, "
        if (flags == House_Balance):
            badges += "Balance, "
        if (flags == Early_Supporter):
            badges += "Early Supporter, "
        if (flags == Bug_Hunter_Level_2):
            badges += "Gold BugHunter, "
        if (flags == Early_Verified_Bot_Developer):
            badges += "Verified Bot Developer, "
        if (flags == Early_Verified_Bot_Developer):
            badges += "Verified Bot Developer, "
        if (badges == ""):
            badges = "None"

        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        avatar_id = r.json()['avatar']
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=sesheaders)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            from datetime import datetime
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
            
        clearprint()
        print(f'''                                   {o}[{m}MAIL{o}]{w} {email}
                                   {o}[{m}PHONE{o}]{w} {phone}
                                   {o}[{m}2FA{o}]{w} {mfa}

                                   {o}[{m}USER ID{o}]{w} {userID}
                                   {o}[{m}USER{o}]{w} {userName}
                                   {o}[{m}NITRO{o}]{w} {has_nitro} / {days_left if has_nitro else "0"} days
                                   {o}[{m}BADGES{o}]{w} {badges}''')
    
        input(f'\n                                      {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back!')
            
    except Exception as e:
        print(f'                                   {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} {e}')
        sleep(0.5)
