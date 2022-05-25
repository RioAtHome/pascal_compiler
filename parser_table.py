# PARSING_TABLE = [
# ["program","id",";",".","array","[","num","..","]","of","integer","real","function",":","procedure","l#","r#","begin","end","if","then","while","do","else","not","+","-",",","var","*","/","div","mod","and","=",">","<","<=",">=","<>","or",":=","$"]
# ,
# [1,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["",2,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","",4,"","","","","",3,3,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","",5,6,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","",7,"",7,"","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","",8,"",8,"","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","",9,"",10,"","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","",12,"","","","","","","","","","",12,"",11,"","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["",13,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","","","","","","",14,"","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["",15,"","","","","","","","","","","","","","","",15,16,15,"",15,"","","","","","","","","","","","","","","","","","","","",""]
# ,["",17,"","","","","","","","","","","","","","","",17,"",17,"",17,"","","","","","","","","","","","","","","","","","","","",""]
# ,["",19,"","","","","","","","","","","","","","","",20,"",21,"",22,"","","","","","","","","","","","","","","","","","","","",""]
# ,["","",24,"","","","","","","","","","","","","","","",24,"","","","",24,"","","","","","","","","","","","","","","","","","",""]
# ,["",25,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","",26,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",27,""]
# ,["",28,"","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","",30,"","","","","","","","","","","","",29,"","",30,"","","","",30,"","","","","","","","","","","","","","","","","","",""]
# ,["",31,"","","","",31,"","","","","","","","",31,"","","","","","","","",31,31,31,"","","","","","","","","","","","","","","",""]
# ,["",32,"","","","",32,"","","","","","","","",32,"","","","","","","","",32,32,32,"","","","","","","","","","","","","","","",""]
# ,["","",34,"","","","","",34,"","","","","","","",34,"",34,"",34,"",34,34,"","","",34,"","","","","","",33,33,33,33,33,33,"","",""]
# ,["",35,"","","","",35,"","","","","","","","",35,"","","","","","","","",35,36,36,"","","","","","","","","","","","","","","",""]
# ,["",37,"","","","",37,"","","","","","","","",37,"","","","","","","","",37,"","","","","","","","","","","","","","","","","",""]
# ,["","",39,"","","","","",39,"","","","","","",38,39,"",39,"",39,"",39,39,"",39,39,39,"",39,39,39,39,39,39,39,39,39,39,39,39,"",""]
# ,["",40,"","","","",41,"","","","","","","","",42,"","","","","","","","",43,"","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","","","","","","","","","","","","","","",44,45,"","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","","",47,"","","","","","","","","","","","","",46,"","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","","","","","","","","","","","","","","","","","",48,"","","","","","","","","","","","","",""]
# ,["","",50,"","","","","","","","","",50,"",50,"","",50,"","","","","","","","","","",49,"","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","",51,"",51,"","",52,"","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","",53,"","","","","","","","","","","","","",54,"","","","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","",55,"","","","","","","","","","","","","","","",56,"","","","","","","","","","","","","","","","","","","","","","","",""]
# ,["","","","","","","","","","","","","","","","",58,"","","","","","","","","","",57,"","","","","","","","","","","","","","",""]
# ,["","",60,"","","","","",60,"","","","","","","",60,"",60,"",60,"",60,60,"",59,59,60,"","","","","","",60,60,60,60,60,60,59,"",""]
# ,["","",62,"","","","","",62,"","","","","","","",62,"",62,"",62,"",62,62,"",62,62,62,"",61,61,61,61,61,62,62,62,62,62,62,62,"",""]
# ,["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",63,64,65,66,67,"","","","","","","","",""]
# ,["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",68,69,70,71,72,73,"","",""]
# ,["","","","","","","","","","","","","","","","","","","","","","","","","",74,75,"","","","","","","","","","","","","",76,"",""]
# ,["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",77,""]
# ]

import production_rules
PARSING_TABLE = {
    "header":{"program":1},
    "identifier_list":{"id": 1},
    "type_":{"integer":1, "real":1, "array": 2},
    "standard_type":{"integer":1, "real": 2},
    "subprogram_declarations":{"function": 1, "procedure": 1, "begin": 1},
    "subprogram_declaration":{"function": 1, "procedure": 1},
    "subprogram_head":{"function": 1, "procedure": 2},
    "args":{";":1, ":": 1, "(": 2},
    "parameter_list":{"id", 1},
    "compound_statement":{"begin":1},
    "optional_statements":{"id":1, "begin":1, "end":2, "if":1, "while":1},
    "statement_list":{"id":1, "begin":1, "if":1, "while":1, },
    "statement":{"id":4, "begin":1, "if":2, "while":3},
    "statement_":{";":2, "[":1, "(":2, "end":2, "else":2, ":=": 1},
    "match_statement":{"else":1},
    "variable":{"id":1},
    "variable_":{"[":1, ":=":2},
    "procedure_statement":{"id":1},
    "procedure_statement_":{";":2, "(":1, "end":2, "else":2},
    "expression_list":{"id":1, "num":1, "(":1, "not":1, "+":1, "-":1},
    "expression":{"id":1, "num":1, "(":1,"not":1, "+":1, "-":1},
    "expression_":{";":2, ")":2, "end":2, "then":2, "do":2, "else":2, ",":2, "=":1, "<":1,"<=":1,">=":1,">":1,"<>":1,},
    "simple_expression":{"id":1,"num":1, "(":1, "not":1, "+":2, "-":2, },
    "term":{"id":1, "num":1, "(":1, "not":1, },
    "factor_":{";":2, "]":2, "(":1, ")":2, "end":2,"then":2, "do":2, "else":2, "+":2, "-":2, ",":2, "*":2,"/":2,'div':2,"mod":2,"and":2, "=":2, "<":2,"<=":2,">=":2,">":2,"<>":2, "or":2},
    "factor":{"id":1, "num":2, "(":3, "not":4},
    "sign":{"+":1, "-":2},
    "identifier_list_":{":":2,",":1},
    "declarations":{"function":1, "procedure":1,"begin":1, "var":1},
    "declarations_":{"function":2, "procedure":2,"begin":2, "var":1},
    "subprogram_declarations_":{"function":1, "procedure":1,"begin":2},
    "parameter_list_":{";":1, ")":2},
    "statement_list_":{";":1, "end":2},
    "expression_list_":{")":2, ",":1},
    "simple_expression_":{";":2, ")":2, "end":2, ",":2, "]":2, "then":2, "do":2, "else":2, "+":1, "-":1, ",":2,"*":2,"/":2,'div':2,"mod":2,"and":2, "=":2, "<":2,"<=":2,">=":2,">":2,"<>":2, "or":1},
    "term_":{";":2, ")":2, "end":2, ",":2,"]":2, "then":2,"do":2, "else":2, "+":2, "-":2,",":2, "*":1, "/":1, "div":1, "mod":1, "and":1, "*":2,"/":2,'div':2,"mod":2,"and":2, "=":2, "<":2,"<=":2,">=":2,">":2,"<>":2, "or":2},
    "mulop":{"*":1,"/":2,'div':3,"mod":4,"and":5},
    "relop":{"=":1, ">":2,"<":3,"<=":4,">=":5,"<>":6},
    "addop":{"+":1, "-":2, "or":3},
    "assignop":{":=":1},

}
production_mapping = {
    "header":production_rules.header,
    "identifier_list":production_rules.identifier_list,
    "identifier_list_":production_rules.identifier_list_,
    "type_":production_rules.type_,
    "standard_type":production_rules.standard_type,
    "subprogram_declarations":production_rules.subprogram_declarations,
    "subprogram_declaration":production_rules.subprogram_declaration,
    "subprogram_head":production_rules.subprogram_head,
    "args":production_rules.args,
    "parameter_list":production_rules.parameter_list,
    "compound_statement":production_rules.compound_statement,
    "optional_statements":production_rules.optional_statements,
    "statement_list":production_rules.statement_list,
    "statement":production_rules.statement,
    "statement_":production_rules.statement_,
    "match_statement":production_rules.match_statement,
    "variable":production_rules.variable,
    "variable":production_rules.variable_,
    "procedure_statement":production_rules.procedure_statement,
    "procedure_statement_":production_rules.procedure_statement_,
    "expression_list":production_rules.expression_list_,
    "expression":production_rules.expression_,
    "simple_expression":production_rules.simple_expression,
    "term":production_rules.term_,
    "factor":production_rules.factor,
    "factor_":production_rules.factor_,
    "sign":production_rules.sign,
    "declarations":production_rules.declarations,
    "declarations_":production_rules.declarations_,
    "subprogram_declarations_":production_rules.subprogram_declarations_,
    "parameter_list_":production_rules.parameter_list_,
    "statement_list_":production_rules.statement_list_,
    "expression_list_":production_rules.expression_list_,
    "simple_expression_":production_rules.simple_expression_,
    "term_":production_rules.term_,
    "relop":production_rules.relop,
    "addop":production_rules.addop,
    "mulop":production_rules.mulop,
    "assignop":production_rules.assignop,
}