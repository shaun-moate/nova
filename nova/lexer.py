# TODO implement Lexer as a class ) - is basically a tokenizer, but it usually attaches extra context to the tokens
# Lexer will define scopes for those tokens (variables/functions)
from nova.builtins import Builtins
from nova.dataclasses import RawToken, TokenId, Token

class Lexer():
    def __init__(self, raw_tokens: list[RawToken]):
        self.raw_tokens = raw_tokens
        self.tokens = []
        self.lex_tokens_from_file()

    def lex_tokens_from_file(self):
        i = 0
        # TODO is there a better implementation approach than below (the random index jumps.... blah!)
        while i < len(self.raw_tokens):
            if self.raw_tokens[i].string_literal:
                typ, value = self.assign_token_type(self.raw_tokens[i].value, typ="str")
                self.tokens.append(Token(typ, self.raw_tokens[i].location, value))
                i += 1
            elif self.raw_tokens[i].value == "macro":
                name = self.raw_tokens[i+1]
                if name.value in Builtins.BUILTIN_MACRO:
                    assert False, "ERROR: attempting to override a built-in macro {} - not permitted".format(name.value)
                i = self.store_macro_to_builtins(name, self.raw_tokens, i+2)
            elif self.raw_tokens[i].value in Builtins.BUILTIN_MACRO:
                typ, value = self.assign_token_type(self.raw_tokens[i].value, typ="macro")
                self.tokens.append(Token(typ, self.raw_tokens[i].location, value))
                i += 1
            elif self.raw_tokens[i].value == "const":
                name = self.raw_tokens[i+1]
                if name.value in Builtins.BUILTIN_CONST:
                    assert False, "ERROR: attempting to override a built-in constant {} - not permitted".format(name.value)
                else:
                    try:
                        Builtins.BUILTIN_CONST[name.value] = int(self.raw_tokens[i+2].value)
                    except ValueError:
                        pass
                i += 3
            elif self.raw_tokens[i].value in Builtins.BUILTIN_CONST:
                typ, value = self.assign_token_type(self.raw_tokens[i].value, typ='const')
                self.tokens.append(Token(typ, self.raw_tokens[i].location, value))
                i += 1
            elif self.raw_tokens[i].value in Builtins.BUILTIN_OPS:
                typ, value = self.assign_token_type(self.raw_tokens[i].value, typ='op')
                self.tokens.append(Token(typ, self.raw_tokens[i].location, value))
                i += 1
            else:
                typ, value = self.assign_token_type(self.raw_tokens[i].value, typ='int')
                self.tokens.append(Token(typ, self.raw_tokens[i].location, value))
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

