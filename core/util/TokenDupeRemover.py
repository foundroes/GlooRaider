


from core.add.plugins import *


import easygui

def removeduplicates():
    titles(title11)
    lines_seen = set()

    print(f"                             {o}[{w}Do you have tokens in the {dirchecker}{o}]")
    user_input = input(f"\n                              {o}[{m}GLOO{o}]{m} {s}| {o}[{m}INPUT{o}] {s}>{w} ")
    
    input_file_path = "Assets/Input/Tokens.txt"
    output_file_path = "Assets/Output/removedduplicates.txt"

    if os.path.exists(output_file_path):
        open(output_file_path, 'a').write('')

    if user_input.lower() in yeslist:
        clpr()
        path = input_file_path
        with open(path, "r", encoding="utf-8") as input_file:
            for each_line in input_file:
                cleaned_line = each_line.strip()  # Remove leading/trailing whitespaces
                if cleaned_line not in lines_seen:
                    with open(output_file_path, "a", encoding="utf-8") as output_file:
                        output_file.write(cleaned_line + '\n')
                        lines_seen.add(cleaned_line)

    elif user_input.lower() in nolist:
        clpr()
        path = easygui.fileopenbox(default='*.txt', filetypes=['*.txt'], title='GLOO - Select your tokens file.', multiple=False)
        with open(path, "r", encoding="utf-8") as input_file:
            for each_line in input_file:
                cleaned_line = each_line.strip()  # Remove leading/trailing whitespaces
                if cleaned_line not in lines_seen:
                    with open(output_file_path, "a", encoding="utf-8") as output_file:
                        output_file.write(cleaned_line + '\n')
                        lines_seen.add(cleaned_line)

    print(f'                         {o}[{w}Successfully removed duplicates -> assets/output/tokens.txt{o}]')