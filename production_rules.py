# Production rules for Grammar in grammar.txt
def header(production_num=1):
    production_output = ["program", "id", ";", "declarations", "subprogram_declarations", "compound_statement", "."]
    return production_output

def identifier_list(production_num=1):
    return ["id", "identifier_list_"]

def type_(production_num=1):
    if production_num == 1:
        return ["standard_type"]
    elif production_num == 2:
        return ["array", "[", "num", "..", "num", "]", "of", "standard_type"]
    

def standard_type(production_num=1):
    if production_num == 1:
        return ["integer"]
    elif production_num == 2:
        return ["real"]

def subprogram_declarations(production_num=1):
    return ["subprogram_declarations_"]


def subprogram_declaration(production_num=1):
    return ["subprogram_head", "declarations", "compound_statement"]


def subprogram_head(production_num=1):
    if production_num == 1:
        return ["function", "id", "args", ":", "standard_type", ";"]
    elif production_num == 2:
        return ["procedure", "id", "args", ";"]

def args(production_num=1):
    if production_num == 1:
        return []
    elif production_num == 2:
        return ["(", "parameter_list", ")"]

def parameter_list(production_num=1):
    return ["id", "identifier_list_", ":", "type_", "parameter_list_"]

def compound_statement(production_num=1):
    return ["begin", "optional_statements", "end"]


def optional_statements(production_num=1):
    if production_num == 1:
        return ["statement_list"]
    elif production_num == 2:
        return []

def statement_list(production_num=1):
    return ["statement", "statement_list_"]


def statement(production_num=1):
    if production_num == 1:
        return ["begin", "optional_statements", "end"]
    elif production_num == 2:
        return ["if", "expression", "then", "statement", "match_statement"] 
    elif production_num == 3:
        return ["while", "expression", "do", "statement"]
    elif production_num == 4:
        return ["id", "statement_"]

def statement_(production_num=1):
    if production_num == 1:
        return ["variable_", "assignop", "expression"]
    if production_num == 2:
        return ["procedure_statement_"]

def match_statement(production_num=1):
    return ["else", "statement"]

def variable(production_num=1):
    return ["id", "variable_"]

def variable_(production_num=1):
    if production_num == 1:
        return ["[", "expression", "]"]
    if production_num == 2:
        return []

def procedure_statement(production_num=1):
    return ["id", "procedure_statement_"]

def procedure_statement_(production_num=1):
    if production_num == 1:
        return ["(", "expression_list", ")"]
    if production_num == 2:
        return []

def expression_list(production_num=1):
    return ["expression", "expression_list_"]


def expression(production_num=1):
    if production_num == 1:
        return ["simple_expression", "expression_"]

def expression_(production_num=1):
    if production_num == 1:
        return ["relop", "simple_expression"]
    elif production_num == 2:
        return []

def simple_expression(production_num=1):
    if production_num == 1:
        return ["term", "simple_expression_"]
    if production_num == 2:
        return ["sign", "term", "simple_expression_"]


def term(production_num=1):
    return ["factor", "term_"]


def factor(production_num=1):
    if production_num == 1:
        return ["id", "factor_"]

    elif production_num == 2:
        return ["num"]
    elif production_num == 3:
        return ["(", "expression", ")"]
    elif production_num == 4:
        return ["not", "factor"]

def factor_(production_num=1):
    if production_num == 1:
        return ["(", "expression_list", ")"]
    elif production_num == 2:
        return []

def sign(production_num=1):
    if production_num == 1:
        return ["+"]
    elif production_num == 2:
        return ["-"]

def identifier_list_(production_num=1):
    if production_num == 1:
        return [",", "id", "identifier_list_"]
    elif production_num == 2:
        return []

def declarations(production_num=1):
    return ["declarations_"]

def declarations_(production_num=1):
    if production_num == 1:
        return ["var", "identifier_list", ":", "type_", ";"]
    if production_num == 2:
        return []

def subprogram_declarations_(production_num=1):
    if production_num == 1:
        return ["subprogram_declaration", ";", "subprogram_declarations_"]
    elif production_num == 2:
        return []

def parameter_list_(production_num=1):
    if production_num == 1:
        return [";", "identifier_list", ":", "type_", "parameter_list_"]
    elif production_num == 2:
        return []    


def statement_list_(production_num=1):
    if production_num == 1:
        return [";", "statement", "statement_list_"]
    elif production_num == 2:
        return []


def expression_list_(production_num=1):
    if production_num == 1:
        return [",", "expression", "expression_list_"]
    elif production_num == 2:
        return []


def simple_expression_(production_num=1):
    if production_num == 1:
        return ["addop", "term", "simple_expression_"]
    elif production_num == 2:
        return []


def term_(production_num=1):
    if production_num == 1:
        return ["mulop", "factor", "term_"]
    elif production_num == 2:
        return []


def relop(production_num=1):
    if production_num == 1:
        return ["="]
    elif production_num == 2:
        return [">"]
    elif production_num == 3:
        return ["<"]
    elif production_num == 4:
        return ["<="]
    elif production_num == 5:
        return [">="]
    elif production_num == 6:
        return ["<>"]


def addop(production_num=1):
    if production_num ==1:
        return ["+"]
    elif production_num == 2:
        return ["-"]
    elif production_num == 3:
        return ["or"]


def mulop(production_num=1):
    if production_num == 1:
        return ["*"]
    elif production_num == 2:
        return ["/"]
    elif production_num == 3:
        return ["div"]
    elif production_num == 4:
        return ["mod"]
    elif production_num == 5:
        return ["and"]

def assignop(production_num=1):
    return [":="]
