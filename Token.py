from enum import Enum
from typing import Any

class TokenType(Enum):
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    INT = "INT"
    FLOAT = "FLOAT"

    PLUS = "PLUS"
    MINUS = "MINUS"
    ASTERISK = "ASTERISK"
    SLASH = "SLASH"
    POW = "POW"
    MODULUS = "MODULUS"

    SEMICOLON = "SEMICOLON"
    LPARENT = "LPARENT"
    RPARENT = "RPARENT"

class Token:
    def __init__(self, type: TokenType, literal: Any, line_no: int, position: int) -> None:
        self.type = type
        self.literal = literal
        self.line_no = line_no
        self.position = position

    def __str__(self) -> str:
        return f"Token[{self.type} : {self.literal} : Line {self.line_no} : position {self.position}]"

    def __repr__(self) -> str:
        return str(self)
