# TODO implement Lexer as a class ) - is basically a tokenizer, but it usually attaches extra context to the tokens
# Lexer will define scopes for those tokens (variables/functions)
from nova.tokenizer import Tokenizer
from nova.builtins import Builtins
from nova.dataclasses import RawToken, TokenId, Token

class Lexer():
    def __init__(self, file_path):
        self.file_path = file_path
        self.tokens = []
        self.tokenizer = Tokenizer(self.file_path)
        tokens = self.tokenizer.raw_tokens
        self.add_token_type(tokens)

    def add_token_type(self, tokens: list[RawToken]):
        i = 0
        while i < len(tokens):
            if tokens[i].string_literal:
                typ, value = self.assign_token_type(tokens[i].value, typ="str")
                self.tokens.append(Token(typ, tokens[i].location, value))
                i += 1
            elif tokens[i].value == "macro":
                name = tokens[i+1]
                if name.value in Builtins.BUILTIN_MACRO:
                    assert False, "ERROR: attempting to override a built-in macro {} - not permitted".format(name.value)
                i = self.store_macro_to_builtins(name, tokens, i+2)
            elif tokens[i].value in Builtins.BUILTIN_MACRO:
                typ, value = self.assign_token_type(tokens[i].value, typ="macro")
                self.tokens.append(Token(typ, tokens[i].location, value))
                i += 1
            elif tokens[i].value == "const":
                name = tokens[i+1]
                if name.value in Builtins.BUILTIN_CONST:
                    assert False, "ERROR: attempting to override a built-in constant {} - not permitted".format(name.value)
                else:
                    try:
                        Builtins.BUILTIN_CONST[name.value] = int(tokens[i+2].value)
                    except ValueError:
                        pass
                i += 3
            elif tokens[i].value in Builtins.BUILTIN_CONST:
                typ, value = self.assign_token_type(tokens[i].value, typ='const')
                self.tokens.append(Token(typ, tokens[i].location, value))
                i += 1
            elif tokens[i].value in Builtins.BUILTIN_OPS:
                typ, value = self.assign_token_type(tokens[i].value, typ='op')
                self.tokens.append(Token(typ, tokens[i].location, value))
                i += 1
            else:
                typ, value = self.assign_token_type(tokens[i].value, typ='int')
                self.tokens.append(Token(typ, tokens[i].location, value))
                i += 1

    def assign_token_type(self, token: str, typ: str):
        if typ == "str":
            return TokenId.STR, bytes(token, "utf-8").decode("unicode_escape")
        elif typ == "macro":
            return TokenId.MACRO, token
        elif typ == "const":
            return TokenId.CONST, token
        elif typ == "op":
            return TokenId.OP, token
        else:
            try:
                return TokenId.INT, int(token)
            except ValueError:
                assert False, "ERROR: unknown operand"

    def store_macro_to_builtins(self, name: RawToken, tokens: list[RawToken], index: int):
        macro_stack = []
        while tokens[index].value != "end":
            macro_stack.append(tokens[index].value)
            index += 1
        Builtins.BUILTIN_MACRO[name.value] = macro_stack
        return index+1

