import sys
import os
from lexical_analysis import Analyzer
from parser_table import PARSING_TABLE, production_mapping
from keywords import KEYWORDS



class SyntaxError(Exception):
    def __init__(self, expected, input_token, line_no):
        self.expected = expected
        self.input_token = input_token
        self.line_no = line_no
    def __str__(self):
        return f"Expected:'{self.expected}', got '{self.input_token}' at Line: {self.line_no}"


class Parser:
    def __init__(self, pascal_file, debug=False):
        self.debug = debug
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
            if self.debug == True:
                print(f"BUFFER --> {self.buffer}\n")
                print(f"TOKEN --> {self.input_token}")
                print("--------------------------------------------")

            if(self.peek == self.input_token['Name']):
                self.buffer.pop()
                try:
                    self.input_token = next(self.token)
                except StopIteration:
                    pass
                if self.input_token["Type"] == 1:
                    self.input_token["Name"] = "num"
                elif self.input_token["Type"] == 2:
                    self.input_token["Name"] = "id"
            elif(self.peek in self.terminals):
                raise SyntaxError(self.peek, self.input_token["Name"], self.input_token["Line No"])
            
            elif(self.input_token["Name"] not in PARSING_TABLE[self.peek]):
                raise SyntaxError(list(PARSING_TABLE[self.peek].keys()), self.input_token["Name"], self.input_token["Line No"])
            
            elif(self.input_token["Name"] in PARSING_TABLE[self.peek]):
                production_num = PARSING_TABLE[self.peek][self.input_token["Name"]]
                production = production_mapping[self.peek](production_num)
                self.buffer.pop()
                
                self.add_to_buffer(production)
            self.peek = self.buffer[-1]
        print("Syntax is A-Okay!")
    

if __name__ == "__main__":
    debug = False
    try:
        file = sys.argv[1]
    except IndexError:
        print("Please Enter file Location...")
        sys.exit()
    try:
        debug = sys.argv[2]
        debug = True
    except IndexError:
        pass

    if os.path.exists(file):
        parser = Parser(file, debug=debug)
        parser.parse()
    else:
        print("Cant find file!")
        sys.exit()
