from pypresence import Presence

import threading
import time

CLIENT_ID = '1290520544923357194'
RPC = Presence(CLIENT_ID)

def RPCstart():
    try:
        RPC.connect()

        RPC.update(
            state="Free & Premium available!",
            details="Website: gloo.lol",

            large_image="https://i.postimg.cc/L8P7qXqY/smaller.png",  
            large_text="gloo.lol",

            small_image="https://i.postimg.cc/L8P7qXqY/smaller.png",      
            small_text="gloo.lol",      

            start=time.time()       
        )
        
        while True:
            time.sleep(15)

    finally:
        RPC.close()

def BackgroundRPC():
    thread = threading.Thread(target=RPCstart, daemon=True)
    thread.start()