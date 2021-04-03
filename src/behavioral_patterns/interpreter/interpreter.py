from enum import Enum
import ast


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LEFT_PAREN = 3
        RIGHT_PAREN = 4

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f"'{self.text}'"


def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif input[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif input[i] == "(":
            result.append(Token(Token.Type.LEFT_PAREN, "("))
        elif input[i] == ")":
            result.append(Token(Token.Type.RIGHT_PAREN, ")"))
        else:
            # must be a number
            digits = []
            j = i
            while input[j].isdigit():
                digits.append(input[j])
                j += 1

            i = j
            result.append(Token(Token.Type.INTEGER, "".join(digits)))
        i += 1

    return result


def calc(input: str):
    tokens = lex(input)
    print(" ".join(map(str, tokens)))


if __name__ == "__main__":
    calc("(13 + 4) - (12 + 1)")  # math expression
    # print(ast.parse('(13 + 4) - (12 + 1)'))
    print(ast.dump(ast.parse("(13 + 4) - (12 + 1)", mode="eval")))
    print(eval("(13 + 4) - (12 + 1)"))
