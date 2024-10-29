from typing import Any
from Token import TokenType, Token

class Lexer:
    def __init__(self, source: str) -> None:
        self.source = source
        self.position: int = -1
        self.read_positon: int = 0
        self.line_no: int = 1
        self.current_char: str | None = None
        self.__read_char()

    def __read_char(self) -> None:
        if self.read_positon >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.read_positon]

        self.position = self.read_positon
        self.read_positon += 1

    def __skip_whitespace(self) -> None:
        while self.current_char in [" ", "\t", "\n", "\r"]:
            if self.current_char == "\n":
                self.line_no += 1

            self.__read_char()

    def __new_token(self, tt: TokenType, literal: Any) -> Token:
        return Token(type=tt, literal=literal, line_no=self.line_no, position=self.position)

    def __is_digit(self, ch: str) -> bool:
        return "0" <= ch and ch <= "9"

    def __read_number(self) -> Token:
        start_position: int = self.position
        dot_count: int = 0
        output: str = ""

        while self.__is_digit(self.current_char) or self.current_char == ".":
            if self.current_char == ".":
                dot_count += 1

            if dot_count > 1:
                print(f"too many decimals in number on line {self.line_no}, position {self.position}")
                return self.__new_token(TokenType.ILLEGAL, self.source[start_position:self.position])

            output += self.source[self.position]
            self.__read_char()

            if self.current_char is None:
                break

        if dot_count == 0:
            return self.__new_token(TokenType.INT, int(output))
        else:
            return self.__new_token(TokenType.FLOAT, float(output))

    def next_token(self) -> Token:
        token: Token = None
        self.__skip_whitespace()

        match self.current_char:
            case "+":
                token = self.__new_token(TokenType.PLUS, self.current_char)
            case "-":
                token = self.__new_token(TokenType.MINUS, self.current_char)
            case "*":
                token = self.__new_token(TokenType.ASTERISK, self.current_char)
            case "/":
                token = self.__new_token(TokenType.SLASH, self.current_char)
            case "%":
                token = self.__new_token(TokenType.MODULUS, self.current_char)
            case "^":
                token = self.__new_token(TokenType.POW, self.current_char)
            case "(":
                token = self.__new_token(TokenType.LPARENT, self.current_char)
            case ")":
                token = self.__new_token(TokenType.RPARENT, self.current_char)
            case ";":
                token = self.__new_token(TokenType.SEMICOLON, self.current_char)
            case None:
                token = self.__new_token(TokenType.EOF, "")
            case _:
                if self.__is_digit(self.current_char):
                    token = self.__read_number()
                    return token
                else:
                    token = Token(TokenType.ILLEGAL, self.current_char)

        self.__read_char()
        return token


