
from core.add.plugins import *


def formater(): # FUNCTION CALL
    titles(title1)

    success = 0 # success counter
    failure = 0 # failure counter
    

    # FUNCTION START
    tokens = get_tokens()
    time_rn = get_time_rn()
    with open("assets/input/tokens.txt", "w") as output_file: # Prints [success, failure] # structure
        for token in tokens:
            if ":" in token:
                token_parts = token.strip().split(":")[2:]  
                new_token = ":".join(token_parts) + "\n"  
                output_file.write(new_token)
                success += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lg}[{g}SUCCESS{lg}] {s}| {w}{token[:37]} {o}[{m}+++{o}]")
                sleep(0.02)
            else:
                failure += 1
                print(f"                      {o}[{m}{time_rn}{o}] {lr}[{r}FAILURE{lr}] {s}| {w}{token[:37]} {o}[{m}---{o}]")
                sleep(0.02)
                output_file.write(token)


    clpr()
        

    print(f'                              {o}[{w}Type {o}"{m}show{o}"{w} for info or press {o}"{m}enter{o}"{w} to go back{o}]\n')
    choose = input(f"                               {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} ")


    if choose == "show": # Call information print
        clpr()
        print(f"""                      {lg}[{g}SUCCESS{lg}] {s}| {o}[{m}{success:03}{o}] {s}>{w} Tokens were sorted and rewritten in tokens.txt!
                      {lr}[{r}FAILURE{lr}] {s}| {o}[{m}{failure:03}{o}] {s}>{w} Tokens failed due to "colon not being found".\n""")
        input(f"                      {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press Enter to go back.")
    

    elif choose == "":
        pass
