from Lexer import Lexer

LEXER_DEBUG: bool = True

if __name__ == "__main__":
    print("running")
    with open("tests/lexer.fred", "r") as f:
        code: str = f.read()

    if LEXER_DEBUG:
        debug_lexer: Lexer = Lexer(source=code)
        while debug_lexer.current_char is not None:
            print(debug_lexer.current_char)
            print(debug_lexer.next_token())
            print(debug_lexer.current_char)
