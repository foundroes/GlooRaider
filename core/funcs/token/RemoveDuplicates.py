from core import *

def RemoveDupes():
    titles('DUPE')

    print(f"                             {o}[{w}Do you have tokens in the {checktokens}{o}]")
    user_input = input(f'                              {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}]{s}>{w} ')

    inputpath = checktokens

    if user_input.lower() in yeslist:
        clearprint()
        with open(inputpath, "r", encoding="utf-8") as input_file:
            lines = input_file.readlines()
        
        unique_lines = set(line.strip() for line in lines)

        with open(inputpath, "w", encoding="utf-8") as output_file:
            for line in unique_lines:
                output_file.write(line + '\n')

    elif user_input.lower() in nolist:
        clearprint()
        path = easygui.fileopenbox(default='*.txt', filetypes=['*.txt'], title='GLOO - Select your tokens file.', multiple=False)
        with open(path, "r", encoding="utf-8") as input_file:
            lines = input_file.readlines()
        
        unique_lines = set(line.strip() for line in lines)

        with open(inputpath, "w", encoding="utf-8") as output_file:
            for line in unique_lines:
                output_file.write(line + '\n')

    clearprint()
    print(f'                                  {o}[{w}Successfully removed and replaced tokens{o}]')
    input(f"\n                                   {o}[{m}GLOO{o}] {s}| {o}[{m}INPUT{o}] {s}>{w} Press ENTER to go back.{d}")
