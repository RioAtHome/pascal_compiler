import sys
import os
from lexical_analysis import Analyzer
from parser_table import PARSING_TABLE, production_mapping

def parser(pascal_file):
	lex = Analyzer(pascal_file)
	token = lex.next_token()
	input_token = next(token)
	buffer = ["$", 1]
	lookahead = buffer[-1]

	while(lookahead != '$'):
		if(lookahead = input_token['Name']):
			buffer.pop()
			input_token = next(token)
		elif(!lookahead.isnumeric()):
			raise error
		elif(PARSING_TABLE[])


	
	

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except IndexError:
        print("Please Enter file Location...")
        sys.exit()

    if os.path.exists(file):
        symbol_table = []
        parser = parser(file)
    else:
        print("Cant find file!")
        sys.exit()
