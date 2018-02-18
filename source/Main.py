from Lexer import Lexer
from Parser import Parser
from AST import AST

def getAST(data):
    res = Lexer.lex(data)
    #print (res)
    ast, res = Parser.parse(res)
    #print(ast.prettyPrint())
    if len(res) > 0:
        print("Cannot Parse: ", res)

    return ast

def main():

    while (True):
        ch = int(input('1. Satisfiability, Unsatistiability and Tautology\n2. Entailment\nSelect: '))
        if ch == 1:
            data = getAST(input('Enter Propositional Formula: '))

            myDict = {"true": True, "TRUE": True, "True": True,
                    "false": False, "FALSE": False, "False": False}

            mySet = data.findVariables(set())
            print ("Satisfiable: ", data.satisfiable(mySet, myDict))
            mySet = data.findVariables(set())
            print ("Unsatisfiable: ", data.unsatisfiable(mySet, myDict))
            mySet = data.findVariables(set())
            print ("Tautology: ", data.tautology(mySet, myDict), '\n\n')

        elif ch == 2:
            data1 = getAST(input('Enter a such that a |= b: '))
            data2 = getAST(input('Enter b such that a |= b: '))

            data = AST(data1, AST(None, data2, '~'), '/\\')

            mySet = data.findVariables(set())
            myDict = {"true": True, "TRUE": True, "True": True,
                    "false": False, "FALSE": False, "False": False}

            print ("Entailment: ", (not data.unsatisfiable(mySet, myDict)), '\n\n')

if __name__ == "__main__":
    main()