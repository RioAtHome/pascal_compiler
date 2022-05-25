import sys
import os
from lexical_analysis import Analyzer
from parser_table import PARSING_TABLE, production_mapping
from keywords import KEYWORDS

class SyntaxError(Exception):
    pass


class Parser:
    def __init__(self, pascal_file):
        self.lex = Analyzer(pascal_file)
        self.token = self.lex.next_token()
        self.input_token  = next(self.token)
        self.buffer = ["$", "header"]
        self.peek = self.buffer[-1]
        self.non_terminals = list(PARSING_TABLE.keys())
        self.terminals = KEYWORDS

    def add_to_buffer(self, production_rule):
        for symbol in reversed(production_rule):
            self.buffer.append(symbol)

    def parse(self): # ie match()      
        while(self.peek != '$'):
            print(f"BUFFER::::{self.buffer}")
            print(self.input_token)
            print("-----------------------------------")
            if self.input_token["Type"] == 1:
                self.input_token["Name"] = "num"
            elif self.input_token["Type"] == 2:
                self.input_token["Name"] = "id"
            if(self.peek == self.input_token['Name']):
                self.buffer.pop()
                self.input_token = next(self.token)
                self.terminals = KEYWORDS
            elif(self.peek in self.terminals):
                raise SyntaxError("peek is terminal")
            elif(self.input_token["Name"] not in PARSING_TABLE[self.peek]):
                raise SyntaxError("not expected")
            elif(self.input_token["Name"] in PARSING_TABLE[self.peek]):
                production_num = PARSING_TABLE[self.peek][self.input_token["Name"]]
                production = production_mapping[self.peek](production_num)
                self.buffer.pop()
                self.add_to_buffer(production)
            self.peek = self.buffer[-1]


    
    

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("Please Enter file Location...")
        sys.exit()

    if os.path.exists(file):
        parser = Parser(file)
        parser.parse()
    else:
        print("Cant find file!")
        sys.exit()
