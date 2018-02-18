from AST import AST

class Parser:

    @staticmethod
    def parse(input = []):
        return Parser.parseBiconditional(input);

        #if len(input) > 0:


    @staticmethod
    def parseNegation(input = []):
        #ast, input = Parser.parseProduct(input)

        if len(input) is 0:
            return None, input

        if input[0] == '~':
            ast, input = Parser.parseNegation(input[1:])
            ast = AST(None, ast, '~')
            return ast, input

        return Parser.parseAtom(input)

    @staticmethod
    def parseConjunction(input = []):
        ast, input = Parser.parseNegation(input)

        if len(input) is not 0 and input[0] == '/\\':
            ast2, input = Parser.parseConjunction(input[1:])
            ast = AST(ast, ast2, '/\\')

        return ast, input

    @staticmethod
    def parseDisjunction(input = []):
        ast, input = Parser.parseConjunction(input)

        if len(input) is not 0 and input[0] == '\\/':
            ast2, input = Parser.parseDisjunction(input[1:])
            ast = AST(ast, ast2, '\\/')

        return ast, input

    @staticmethod
    def parseImplication(input = []):
        ast, input = Parser.parseDisjunction(input)

        if len(input) is not 0 and input[0] == '==>':
            ast2, input = Parser.parseImplication(input[1:])
            ast = AST(ast, ast2, '==>')

        return ast, input

    @staticmethod
    def parseBiconditional(input = []):
        ast, input = Parser.parseImplication(input)

        if len(input) is not 0 and input[0] == '<=>':
            ast2, input = Parser.parseBiconditional(input[1:])
            ast = AST(ast, ast2, '<=>')

        return ast, input

    @staticmethod
    def parseAtom(input):
        if input  == []:
            print ("Error At parseAtom!")
            return

        if len(input) is not 0 and input[0] == '(':
            ast, input = Parser.parseBiconditional(input[1:])
            if input[0] == ')':
                return ast, input[1:]

        #return AST(None, None, Parser.boolTryParse(input[0])), input[1:]
        return AST(None, None, input[0]), input[1:]

    @staticmethod
    def boolTryParse(value):
        try:
            return bool(value)
        except ValueError:
            return value