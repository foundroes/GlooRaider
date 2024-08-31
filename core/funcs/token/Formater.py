from core import *

def Formatter(): 
    clearprint()
    titles('FORMATTER')

    success = 0 
    failure = 0 
    
    tokens = getting.get_tokens()  # Use get_tokens to fetch the list of tokens
    time_rn = getting.get_time_rn()

    with open("assets/input/tokens.txt", "w", encoding='utf-8') as output_file: 
        for token in tokens:
            if ":" in token:
                token_parts = token.strip().split(":")[2:]  
                new_token = ":".join(token_parts) + "\n"  
                output_file.write(new_token)
                success += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}| {w}{token[:37]} {o}[{m}+++{o}]")
                sleep(0.01)
            else:
                failure += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}| {w}{token[:37]} {o}[{m}---{o}]")
                sleep(0.01)
                output_file.write(token + "\n")

    clearprint()
        
    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")

    if choose == "show": 
        clearprint()
        print(f"""                     {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Tokens were sorted and rewritten in tokens.txt!
                     {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Tokens failed due to "colon not being found".\n""")
        input(f"                     {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.")
    
    elif choose == "": 
        pass

