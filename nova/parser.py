# Parser - takes the stream of tokens from the lexer and turns it into an abstract syntax tree representing the (usually) program represented by the original text. 
# Parser then will build the code/program structure
from nova.builtins import Builtins
from nova.dataclasses import Token, OperandId, TokenId, Operand, Program

# TODO Add typing to functions including expected return types
class Parser():
    def __init__(self, tokens: list[Token]):
        self.program = Program()
        self.tokens = tokens
        self.generate_program()

    def generate_program(self):
        self.program = self.generate_blocks(
                    Program(operands = [self.parse_token_as_op(token) 
                                        for token in self.tokens])
                )

    def generate_blocks(self, program: Program) -> Program:
        block = []
        program = self.unnest_program(program)
        for ip in range(len(program.operands)):
            assert len(OperandId) == 33, "Exhaustive list of operands"
            if program.operands[ip].action == OperandId.IF:
                block.append(ip)
            if program.operands[ip].action == OperandId.ELSE:
                ref = block.pop()
                assert program.operands[ref].action == OperandId.IF, "ERROR: `else` can only be used in `if` blocks"
                program.operands[ref].action = OperandId.IF
                program.operands[ref].jump_to = ip+1
                block.append(ip)
            if program.operands[ip].action == OperandId.FI:
                ref = block.pop()
                assert program.operands[ref].action == OperandId.IF or program.operands[ref].action == OperandId.ELSE, "ERROR: `fi` is expected to end the blocks for `if` or `else` only"
                program.operands[ip].jump_to = ip+1
                program.operands[ref].jump_to = ip
            if program.operands[ip].action == OperandId.WHILE:
                block.append(ip)
            if program.operands[ip].action == OperandId.DO:
                ref = block.pop()
                assert program.operands[ref].action == OperandId.WHILE, "ERROR: `do` can only be used in `while` blocks"
                program.operands[ip].jump_to = ref
                block.append(ip)
            if program.operands[ip].action == OperandId.DONE:
                ref = block.pop()
                program.operands[ip].jump_to = program.operands[ref].jump_to
                program.operands[ref].action = OperandId.DO
                program.operands[ref].jump_to = ip+1
            if program.operands[ip].action == OperandId.END:
               pass
        return program

    def unnest_program(self, program: Program):
        result = []
        for i in range(len(program.operands)):
            if type(program.operands[i]) is list:
                for j in range(len(program.operands[i])):
                    result.append(program.operands[i][j])
            else:
                result.append(program.operands[i])
        program.operands = result
        return program

    def parse_token_as_op(self, token: Token):
        location = token.location
        if token.typ == TokenId.OP:
            if token.value in Builtins.BUILTIN_OPS:
                return Operand(action   = Builtins.BUILTIN_OPS[token.value],
                               jump_to  = -1,
                               mem_addr = -1,
                               location = location,
                               value    = token.value)
            else:
                print("%s:%d:%d: ERROR: unknown operand `%s` found".format(token.location, (token.value, )))
                exit(1)
        elif token.typ == TokenId.MACRO:
            return [Operand(action   = action,
                            jump_to  = -1,
                            mem_addr = -1,
                            location = token.location,
                            value    = value)
                    for (action, value) in self.lex_macro_from_builtins(token.value)]
        elif token.typ == TokenId.CONST:
            if token.value in Builtins.BUILTIN_CONST:
                return Operand(action   = OperandId.PUSH_INT,
                               jump_to  = -1,
                               mem_addr = -1,
                               location = token.location,
                               value    = Builtins.BUILTIN_CONST[token.value])
        elif token.typ == TokenId.INT:
            return Operand(action   = OperandId.PUSH_INT,
                           jump_to  = -1,
                           mem_addr = -1,
                           location = token.location,
                           value    = token.value)
        elif token.typ == TokenId.STR:
            return Operand(action   = OperandId.PUSH_STR,
                           jump_to  = -1,
                           mem_addr = -1,
                           location = token.location,
                           value    = token.value)
        else:
            assert False, "TokenId type is unreachable is unreachable"

    def lex_macro_from_builtins(self, macro):
        if macro in Builtins.BUILTIN_MACRO:
            instructions = Builtins.BUILTIN_MACRO[macro]
            for token in instructions:
                try:
                    yield(OperandId.PUSH_INT, int(token))
                except:
                    yield(Builtins.BUILTIN_OPS[token], token)
