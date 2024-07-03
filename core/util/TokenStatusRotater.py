

from core.add.plugins import *

def read_statuses(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]

def get_user_info(token):
    header ={
        'authorization': token
    }
    r = requests.get("https://discord.com/api/v10/users/@me", headers=header)
    if r.status_code == 200:
        user_info = r.json()
        return user_info[f"username"] + f"#" + user_info[f"discriminator"], True
    else:
        return f"Token Invalid", False

def statusrotater():
    def change_status(token, message):
        header = {
            'authorization': token
        }

        current_status = requests.get("https://discord.com/api/v8/users/@me/settings", headers=header).json()

        custom_status = current_status.get("custom_status", {})
        if custom_status is None:
            custom_status = {}
        custom_status["text"] = message

        jsonData = {
            "custom_status": custom_status,
            "activities": current_status.get("activities", [])
        }

        response = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=header, json=jsonData)
        return response.status_code

    def read_statuses(file_name):
        with open(file_name, "r") as file:
            return [line.strip() for line in file.readlines()]

    def load_config():
        config = configparser.ConfigParser()
        config.read("config.ini")
        status_rotater_config = config["STATUS"]
        return {
            "status_rotater": {
                "token": status_rotater_config["token"],
                "sleep_interval": status_rotater_config["sleep_interval"] 
            }
        }


    config = load_config()
    token = config["status_rotater"]["token"]  
    sleep_interval = config["status_rotater"]["sleep_interval"]

    status_count = 0  
    invalid_count = 0

    while True:
        user_info, is_valid_token = get_user_info(token)
        statuses = read_statuses("assets/input/status.txt")

        if len(statuses) == 0:
            clpr()
            print(f"                       {o}[{w}No available statuses to rotate. Check assets/input/status.txt{o}]\n")
            input(f"                        {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")
            break

        for status in statuses:
            time_rn = get_time_rn()
            
            if is_valid_token:
                clpr()
                print(f"""                                   {o}[{m}STATUS{o}]{w} {status}
                                   {o}[{m}TOKEN{o}]{w} Valid: {g}{is_valid_token}
                                   {o}[{m}USER{o}]{w} {user_info}
                                   {o}[{m}TIME{o}]{w} {time_rn}""")
                change_status(token, status)
            else:
                invalid_count += 1
                clpr()
                print(f"""                                   {o}[{m}STATUS{o}]{w} {status}
                                   {o}[{m}TOKEN{o}]{w} Valid: {r}{is_valid_token}
                                   {o}[{m}USER{o}]{w} {user_info}
                                   {o}[{m}TIME{o}]{w} {time_rn}""")
                change_status(token, status)
                
            status_count += 1
            time.sleep(float(sleep_interval))
                
        if invalid_count >= 2:
            clpr()
            print(f"                               {o}[{w}Your token became invalid mid status rotation{o}]\n")
            input(f"                                {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")
            break
