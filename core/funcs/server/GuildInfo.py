

from core import *


def GuildInfo():
    titles('SINFO')
    guildId = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}SERVER ID{o}] {s}>{w} ")
    token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d} ")
    
    if not addons.validatetoken(token):
        return  

    if not (guildId and token):
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return
    
    sesheaders = headers.copy()
    sesheaders.update({"Authorization": token})

    response = requests.get(
        f"https://discord.com/api/guilds/{guildId}",
        headers=sesheaders,
        params={"with_counts": True}
    ).json()

    if 'owner_id' in response:
        owner_id = response['owner_id']

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{owner_id}",
            headers=sesheaders,
            params={"with_counts": True}
        ).json()

    clearprint()
    print(f"""                                   {o}[{m}MEMBER COUNT{o}]{w} {response['approximate_member_count']} members
                                   {o}[{m}SERVER ID{o}]{w} {response['id']}
                                   {o}[{m}SERVER NAME{o}]{w} {response['name']} 

                                   {o}[{m}OWNER NAME{o}]{w} {owner['user']['username']}#{owner['user']['discriminator']}
                                   {o}[{m}OWNER ID{o}]{w} {response['owner_id']}
                                   
                                   {o}[{m}REGION{o}]{w} {response['region']}""")
    input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")