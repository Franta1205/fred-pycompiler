from Lexer import Lexer
from Token import TokenType, Token
from typing import Callable
from enum import Enum, auto

class PrecedenceType(Enum):
    P_LOWEST = 0
    P_EQUALS = auto()
    P_LESSGREATER = auto()
    P_SUM = auto()
    P_PRODUCT = auto()
    P_EXPONENT = auto()
    P_PREFIX = auto()
    P_CALL = auto()
    P_INDEX = auto()

PRECEDENCES: dict[TokenType, PrecedenceType] = {
    TokenType.PLUS: PrecedenceType.P_SUM,
    TokenType.MINUS: PrecedenceType.P_SUM,
    TokenType.SLASH: PrecedenceType.P_PRODUCT,
    TokenType.ASTERISK: PrecedenceType.P_PRODUCT,
    TokenType.MODULUS: PrecedenceType.P_PRODUCT,
    TokenType.POW: PrecedenceType.P_EXPONENT
}

class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

        self.errors: list[str] = []
        self.current_token: Token = None
        self.peek_token: Token = None

        self.prefix_parse_fns: dict[TokenType, Callable] = {}
        self.infix_parse_fns: dict[TokenType, Callable] = {}
        self.__next_token()

    def __next_token(self) -> None:
        self.current_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    def __peek_token_is(self, tt: TokenType) -> bool:
        return self.peek_token == tt

    def __expect_peek(self, tt: TokenType):
        if self.__peek_token_is(tt):
            self.__next_token()
            return True
        else:
            self.__peek_err(tt)
            return False

    def _current_precedence(self) -> PrecedenceType:
        prec: int | None = PRECEDENCES.get(self.current_token.type)
        if prec is None:
            return PrecedenceType.P_LOWEST
        return prec

    def _current_precedence(self) -> PrecedenceType:
        prec: int | None = PRECEDENCES.get(self.peek_token.type)
        if prec is None:
            return PrecedenceType.P_LOWEST
        return prec

    def __peek_err(self, tt: TokenType):
        self.errors.append(f"expected next token to be {tt}, got {self.peek_token.type} instead")

    def __no_prefix_parse_fn_err(self, tt: TokenType):
        self.errors.append(f"no prefix parse function found fo {tt}")