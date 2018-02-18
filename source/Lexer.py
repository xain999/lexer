class Lexer:

    space = ['\t', '\n', '\r', '\r\n', ' ']

    punctuation = ['(', ')', '{', '}', '[', ']']

    symbolic = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '-',
                '+', '=', '|', '\\', ':', ';', '<', '>', '.', '?', '/']

    numeric = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    alphabetic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', '_', '\'', 'A', 'B',
                    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'w', 'X', 'Y', 'Z']

    alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', '_', '\'', 'A', 'B',
                    'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'w', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9']

    @staticmethod
    def lexWhile(input, prop = []):

        pos = 0;
        while (pos < len(input)):
            if input[pos] in prop:
                pos = pos + 1;
                continue

            break;

        return input[:pos], input[pos:]

    @staticmethod
    def lex(input):
        if (len(input) < 1):
            return [];

        input = input.replace("~", " ~ ")

        if input[0] in Lexer.space:
            t, input = Lexer.lexWhile(input, Lexer.space)

        if input[0] in Lexer.alphabetic:
            ele, input = Lexer.lexWhile(input, Lexer.alphanumeric)

        elif input[0] in Lexer.symbolic:
            ele, input = Lexer.lexWhile(input, Lexer.symbolic)

        elif input[0] in Lexer.numeric:
            ele, input = Lexer.lexWhile(input, Lexer.numeric)

        #elif input[0] in Lexer.punctuation:
        #    ele, input = Lexer.lexWhile(input, Lexer.punctuation)

        else:
            ele = input[0]
            input = input[1:]

        return [ele] + Lexer.lex(input)
