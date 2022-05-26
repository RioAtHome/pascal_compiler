import sys
import os
from keywords import KEYWORDS

class Analyzer:
    def __init__(self, pascal_file, symbol_table=[]):
        with open(pascal_file, "r+") as file:
            self.input_string = file.read()
            self.input_string = self.input_string.split("\n")
            
        self.input_string = [
            line.replace("  ", " ").strip() for line in self.input_string
        ]
        self.symbol_table = symbol_table
        self.token = {"Name": "", "Type": "", "Line No": 0}

    def put_into_symbol_table(self, name, type_, line):
        self.token["Name"] = name
        self.token["Type"] = type_
        self.token["Line No"] = line

        self.symbol_table.append(self.token)

        return self.token

    def next_token(self):
        line_count = 1
        for line_ in self.input_string:
            for word in line_.split(" "):
                if word == "":
                    continue

                buffer = []
                last_keyword = 0
                if word in KEYWORDS:
                    token = self.put_into_symbol_table(word, 0, line_count)
                    
                    yield token
                    continue
                if word.isnumeric():
                    token = self.put_into_symbol_table(word, 1, line_count)
                    KEYWORDS.append(token["Name"])
                    yield token
                    continue
                for char, index in zip(word, range(len(word))):
                    
                    if char in KEYWORDS:
                        if last_keyword == 0:
                            buffer.append(word[:index])
                            buffer.append(word[index])
                            last_keyword = index
                            continue
                        if last_keyword == index - 1:
                            buffer.append(word[index])
                        else:
                            buffer.append(word[last_keyword + 1 : index])
                            buffer.append(word[index])
                            last_keyword = index
                if last_keyword == 0:
                    token = self.put_into_symbol_table(word, 2, line_count)
                    

                    
                    
                    yield token
                    continue
                for entry in buffer:

                    if entry in KEYWORDS:
                        token = self.put_into_symbol_table(entry, 0, line_count)
                        
                    elif entry.isnumeric():
                        token = self.put_into_symbol_table(entry, 1, line_count)
                        KEYWORDS.append(token["Name"])
                    else:
                        token = self.put_into_symbol_table(entry, 2, line_count)
                        
                        

                    yield token
            line_count += 1


if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("Please Enter file Location...")
        sys.exit()

    if os.path.exists(file):
        symbol_table = []
        analyzer = Analyzer(file, symbol_table)
        get_token = analyzer.next_token()
        for _ in range(100):
            print(next(get_token))

    else:
        print("Cant find file!")
        sys.exit()
