import sys
import os
from keywords import KEYWORDS

token = {
        "Name": "",
        "Type": "",
        "Line No": 0
    }


# def print_token(name, _type, line_number):
#     token["Name"] = name
#     token["Type"] = _type
#     token["Line No"] = line_number
#     print(token)
#     print("\n")


# def lexical_analysis(pascal_file):
#     with open(pascal_file, 'r+') as file:
#         count_line = 0
#         for line in file:
#             count_line += 1
#             # Remove newline char from  line
#             refined_line = line.strip().replace(' ', '').lower()
#             buffer = ''
#             for char in refined_line:
#                 # keep putting each new char into buffer until a keyword is
#                 # met, either one char keyword, or multi char keyword
#                 # if no keyword is met, its either an int or var
#                 buffer += char
#                 if char in KEYWORDS:
#                     buffer = buffer[:-1]
#                     if len(buffer) != 0:
#                         try:
#                             int(buffer)
#                             print_token(buffer, '1', count_line)
#                         except ValueError:
#                             print_token(buffer, '2', count_line)
#                     buffer = ''
#                     print_token(char, '0', count_line)
#                 elif buffer in KEYWORDS:
#                     print_token(buffer, '0', count_line)
#                     buffer = ''
#         buffer = ''

class Analyzer:
    def __init__(self, pascal_file, symbol_table):
        with open(pascal_file, 'r+') as file:
            input_string = file.readlines()
            self.refined_line = ''.join([line.strip() for line in input_string])
        
        self.refined_line = self.refined_line.replace(' ', '').lower()
    def next_token(self):
        pass
               

if __name__ == '__main__':
    try:
        file = sys.argv[1]
    except IndexError:
        print("Please Enter file Location...")
        sys.exit()

    if os.path.exists(file):
        analyzer = Analyzer(file)
    else:
        print("Cant find file!")
        sys.exit()
