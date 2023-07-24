import pytest
from nova.old import *
from nova.builtins import *
from nova.helpers import *
from nova.dataclasses import *



# lex_macro_from_builtins()
def test_lex_macro_from_builtins_as_expected():
    result = list(lex_macro_from_builtins('write'))
    assert result == [(OperandId.PUSH_INT, 1), (OperandId.PUSH_INT, 1), (OperandId.SYSCALL, 'syscall')]

# TODO implement capability to store strings in a macro
# TODO add test to /tests for simulation and compilation test
def test_lex_macro_from_builtins_new_macro_with_string():
    pass
    # line = 'macro hello "Hello!" 1 1 syscall end'
    # name = get_next_symbol(line, 5)
    # store_macro(line, name.value, name.end)
    # result = list(lex_macro_from_builtins('hello'))
    # assert result == [(OperandId.PUSH_INT, 69), (OperandId.DUMP, 'dump')]

# TODO implement ability for use of other macros is a macro (ala. 'write')
# TODO add test to /tests for simulation and compilation test
def test_lex_macro_from_builtins_new_macro_with_macro():
    pass
    # line = 'macro hellomacro "Hello!... macro" write end'
    # name = get_next_symbol(line, 5)
    # store_macro(line, name.value, name.end)
    # result = list(lex_macro_from_builtins('hellomacro'))
    # assert result == [(OperandId.PUSH_INT, 69), (OperandId.DUMP, 'dump')]

# TODO consider implementation of recursive macro
# TODO add test to /tests for simulation and compilation test
def test_lex_macro_from_builtins_new_macro_recursive():
    pass

'''

def parse_program_from_file(input_file_path: str) -> Program:
    with open(input_file_path, "r"):
        return generate_blocks(
                    Program(operands = [parse_token_as_op(token) 
                                        for token in parse_tokens_from_file(input_file_path)])
                )

def unnest_program(program: Program):
    result = []
    for i in range(len(program.operands)):
        if type(program.operands[i]) is list:
            for j in range(len(program.operands[i])):
                result.append(program.operands[i][j])
        else:
            result.append(program.operands[i])
    program.operands = result
    return program


def generate_blocks(program: Program) -> Program:
    block = []
    program = unnest_program(program)
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

def parse_token_as_op(token: Token):
    location = token.location
    assert len(TokenId) == 5, "Exhaustive list of operands in parse_word()"
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
                for (action, value) in lex_macro_from_builtins(token.value)]
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


'''
