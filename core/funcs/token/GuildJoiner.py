from core import *

def TokenJoiner():
    clearprint()
    titles('TJOINER')

    print(f"""                                        {o}[{m}01{o}] {s}>{w} Token Joiner {o}[{m}Solver{o}]
                                        {o}[{m}02{o}] {s}>{w} Token Joiner {o}[{m}No Solver{o}]""")

    whichone = input(f"\n                                        {o}[{m}GLOO{o}] {s}|{w} {o}[{m}INPUT{o}] {s}>{w} ")

    if whichone == "1":
        Premium()
        tknJoiner()
    
    elif whichone == "2":
        tknJoiner()

@dataclass
class JoinerData:
    pass

@dataclass
class Instance(JoinerData):
    client: tls_client.sessions
    token: str
    invite: str
    headers: dict

class Joiner:


    joined = 0
    failed = 0

    def __init__(self, data:Instance) -> None:
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
                Joiner.success += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}|{w} {self.instance.token[:37]} {o}[{m}{result.status_code}{o}]")
            else:
                time_rn = getting.get_time_rn()
                Joiner.failed += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}|{w} {self.instance.token[:37]} {o}[{m}{result.status_code}{o}]")
                
class intilize:
        def start(i):
            Joiner(i).join()

def tknJoiner():

    Joiner.joined = 0
    Joiner.failed = 0

    clearprint()
    tokens = getting.get_tokens()


    threads_value = config['MAIN']['threads']
    max_threads = int(threads_value)

    instances = []
    invite = input(f"                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INVITE{o}] {s}>{w} discord.gg/")
    clearprint()
    for i in range(len(tokens)):

        sesheaders = headers.copy()
        sesheaders.update()

        instances.append(Instance(
            client=tls_client.Session(
            client_identifier=f"chrome_{random.randint(110,115)}",
            random_tls_extension_order=True
        ),
            token=tokens[i],
            headers=sesheaders,
            invite=invite
        ))

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(intilize.start, i) for i in instances]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                time_rn = getting.get_time_rn()
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}ERROR{lr}]   {s}|{w} {e}")

    clearprint()
    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show":
        clearprint()
        print(f"""                             {lg}[{g}JOINED{lg}] {s}| {o}[{m}{Joiner.joined:03}{o}] {s}> {w}Tokens joined the server.
                             {lr}[{r}FAILED{lr}] {s}| {o}[{m}{Joiner.failed:03}{o}] {s}> {w}Tokens failed to join the server.""")
        input(f"\n                             {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back{o}.")
    else:
        pass
