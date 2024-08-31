from core import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from time import sleep

# Your script to inject the token
script = """
let token = "your token";

function login(token) {
    localStorage.setItem('token', token);
    setTimeout(() => {
        location.reload();
    }, 1000);
}

login(token);
"""

def Login():
    titles('LOGIN')
    token = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}TOKEN{o}] {s}> [INPUT HIDDEN]{d}")

    if not addons.validatetoken(token):
        return  

    if not token:
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return
    
    sesheaders = headers.copy()
    sesheaders.update({'Authorization': token})

    clearprint()
    response = requests.get("https://discord.com/api/v9/users/@me", headers=sesheaders)
    if response.status_code == 200:
        j = response.json()
        if "username" in j and "discriminator" in j:
            user = j["username"] + "#" + str(j["discriminator"])
            type_ = getDriver()

            try:
                if type_ == "operadriver.exe":
                    opts = webdriver.ChromeOptions()
                    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
                    opts.add_experimental_option("detach", True)
                    driver = webdriver.Opera(options=opts)
                elif type_ == "msedgedriver.exe":
                    opts = webdriver.EdgeOptions()
                    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
                    opts.add_experimental_option("detach", True)
                    driver = webdriver.Edge(options=opts)
                else:
                    raise ValueError("Unsupported driver type")
                
                driver.get("https://discord.com/login")

                # Wait for the page to load
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

                # Execute the script
                driver.execute_script(script.replace("your token", token))

                sleep(1.5)
                print(f"                             {o}[{m}GLOO{o}] {s}| {o}[{m}INFO{o}] {s}>{w} Logging in @{user}.")
            except sel_exceptions.SessionNotCreatedException as e:
                clearprint()
                sleep(0.5)
                print(f"                                      {o}[{w}Drivers do not match the version{o}]")
                sleep(1.5)
            except Exception as e:
                clearprint()
                print(f"                                      {o}[{w}An error occurred: {str(e)}]")
                sleep(1.5)
        else:
            sleep(0.5)
            print(f"                                            {o}[{w}Invalid API Response{o}]")
            sleep(1.5)
    else:
        print(f"API request failed with status code {response.status_code}")


