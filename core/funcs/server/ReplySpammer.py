from core import *

stop_event = threading.Event()

def ReplySpammer():
    global success, failure, stop_event
    success = 0
    failure = 0
    titles('REPLY')
    
    clearprint()
    output_lock = threading.Lock()

    channel_id = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}CHANNEL ID{o}] {s}>{w} ")
    msg_id = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MESSAGE ID{o}] {s}>{w} ")
    msg = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}MESSAGE{o}] {s}>{w} ")

    if not (channel_id and msg_id and msg):
        clearprint()
        print(f"                                  {o}[{m}GLOO{o}] {s}| {o}[{m}ERROR{o}] {s}>{w} Inputs cannot be empty.")
        sleep(0.7)
        return

    clearprint()

    def reply_spammer(token, channel_id, message_id, msg):
        global success, failure
        while not stop_event.is_set():
            payload = {
                'content': msg,
                'tts': False,
                'message_reference': {
                    "channel_id": channel_id,
                    "message_id": message_id
                }
            }

            sesheaders = headers.copy()
            sesheaders.update({"Authorization": token})

            response = session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=sesheaders, json=payload)
            with output_lock:
                time_rn = getting.get_time_rn()
                if response.status_code in [200, 201, 204]:
                    success += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]{d}")
                elif response.status_code == 429:
                    failure += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]{d}")
                else:
                    failure += 1
                    print(f"                      {o}[{m}{time_rn}{o}] {ly}[{y}LIMITED{ly}]{y} {s}| {w}{token[:37]} {o}[{m}{response.status_code}{o}]{d}")
                time.sleep(0.10)

    tokens = getting.get_tokens()
    
    num_threads = getting.get_num_threads()
    threads = []

    for token in tokens:
        for _ in range(num_threads):
            t = threading.Thread(target=reply_spammer, args=(token, channel_id, msg_id, msg))
            threads.append(t)
            t.start()

    def stop_listener():
        keyboard.wait('x')
        stop_event.set()

    stop_thread = threading.Thread(target=stop_listener, daemon=True) 
    stop_thread.start()

    for t in threads:
        t.join()

    clearprint()

    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clearprint()
        print(f"""                              {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:04}{o}] {s}>{w} Messages sent to the channel from tokens.
                              {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:04}{o}] {s}>{w} Messages were unable to be sent.\n""")
        input(f"                              {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")

    elif choose == "":
        pass
