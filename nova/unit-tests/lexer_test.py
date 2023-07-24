import pytest

from nova.lexer import *
from nova.builtins import *
from nova.helpers import *
from nova.dataclasses import *


# get_next_symbol
def test_get_next_symbol_as_expected():
    line = '69 96 + dump'
    symbol = get_next_symbol(line, start=0) 
    assert symbol == Symbol(start = 0, end = 2, value = '69', string = False)

def test_get_next_symbol_string_case():
    line = '     "this is a string, hello world!"'
    symbol = get_next_symbol(line, start=0) 
    assert symbol == Symbol(start = 5, end = 37, value = 'this is a string, hello world!', string = True)

def test_get_next_symbol_as_list():
    symbol_list = []
    start = 0
    line = '69 96 + dump'
    while start < len(line):
        symbol = get_next_symbol(line, start)
        symbol_list.append(symbol)
        start = symbol.end
    assert symbol_list == [Symbol(start = 0, end = 2, value = '69', string = False), 
                          Symbol(start = 3, end = 5, value = '96', string = False), 
                          Symbol(start = 6, end = 7, value = '+', string = False), 
                          Symbol(start = 8, end = 12, value = 'dump', string = False)]

def test_get_next_symbol_as_list_with_string():
    symbol_list = []
    start = 0
    line = '69 96 + "hello, world!" dump'
    while start < len(line):
        symbol = get_next_symbol(line, start)
        symbol_list.append(symbol)
        start = symbol.end
    assert symbol_list == [Symbol(start = 0, end = 2, value = '69', string = False), 
                          Symbol(start = 3, end = 5, value = '96', string = False), 
                          Symbol(start = 6, end = 7, value = '+', string = False), 
                          Symbol(start = 8, end = 23, value = 'hello, world!', string = True),
                          Symbol(start = 24, end = 28, value = 'dump', string = False)]


# assign_token_type
def test_check_assign_token_type_str():
    token_str = assign_token_type(token="forty-two", typ="str")
    assert token_str == (TokenId.STR, "forty-two")

def test_check_assign_token_type_macro():
    token_macro = assign_token_type(token="forty-two", typ="macro")
    assert token_macro == (TokenId.MACRO, "forty-two")

def test_check_assign_token_type_const():
    token_const = assign_token_type(token="forty-two", typ="const")
    assert token_const == (TokenId.CONST, "forty-two")

def test_check_assign_token_type_int():
    token_int = assign_token_type(token="42", typ="int")
    assert token_int == (TokenId.INT, 42)

def test_check_assign_token_type_int_string_passed_error():
    with pytest.raises(AssertionError):
        assign_token_type(token="forty-two", typ="int")

def test_check_assign_token_type_operand():
    token_op = assign_token_type(token="forty-two", typ="op")
    assert token_op == (TokenId.OP, "forty-two")


# lex_line_to_tokens():
def test_lex_line_to_tokens_as_expected():
    line = '69 96 + dump'
    tokens = list(lex_line_to_tokens(line))
    assert tokens == [
            (0, (TokenId.INT, 69)),
            (3, (TokenId.INT, 96)),
            (6, (TokenId.OP, "+")),
            (8, (TokenId.OP, "dump"))
            ]

def test_lex_line_to_tokens_with_unknown_op_error():
    line = '69 96 + unknown'
    with pytest.raises(AssertionError):
        list(lex_line_to_tokens(line))

def test_lex_line_to_tokens_with_string():
    line = '"Hello, World!" write'
    tokens = list(lex_line_to_tokens(line))
    assert tokens == [
            (0, (TokenId.STR, "Hello, World!")),
            (16, (TokenId.MACRO, "write"))
            ]

def test_lex_line_to_tokens_with_new_macro():
    line = 'macro write669 69 dump end'
    tokens = list(lex_line_to_tokens(line))
    assert tokens == []

def test_lex_line_to_tokens_with_set_macro():
    line = 'macro write96 96 dump end write96'
    tokens = list(lex_line_to_tokens(line))
    assert tokens == [
            (26, (TokenId.MACRO, "write96"))
            ]

def test_lex_line_to_tokens_with_existing_macro_error():
    line = 'macro write 42 dump end'
    with pytest.raises(AssertionError):
        list(lex_line_to_tokens(line))

def test_lex_line_to_tokens_with_set_force_recursive_error():
    line = 'macro write42 42 dump write42 end'
    with pytest.raises(AssertionError):
        list(lex_line_to_tokens(line))

def test_lex_line_to_tokens_with_set_force_without_end_error():
    line = 'macro write412 412 dump'
    with pytest.raises(AssertionError):
        list(lex_line_to_tokens(line))

def test_lex_line_to_tokens_with_new_const():
    line = 'const SIXTY9 69'
    tokens = list(lex_line_to_tokens(line))
    assert tokens == []

def test_lex_line_to_tokens_with_set_const():
    line = 'const NINETY6 96 NINETY6'
    tokens = list(lex_line_to_tokens(line))
    assert tokens == [
            (17, (TokenId.CONST, "NINETY6"))
            ]

def test_lex_line_to_tokens_with_existing_const_error():
    line = 'const CATCH 69'
    with pytest.raises(AssertionError):
        list(lex_line_to_tokens(line))

def test_lex_line_to_tokens_with_set_const_force_must_be_integer_error():
    line = 'const FORTY2 FORTY2'
    with pytest.raises(AssertionError):
        list(lex_line_to_tokens(line))


# store_const():
def test_store_const_as_expected():
    line = 'const TEMP 69'
    name = get_next_symbol(line, 5)
    store_const(line, name.value, name.end)
    assert Builtins.BUILTIN_CONST[name.value] == (TokenId.INT, 69)

def test_store_const_force_error_with_string():
    line = 'const ERROR not_valid'
    name = get_next_symbol(line, 5)
    with pytest.raises(AssertionError):
        store_const(line, name.value, name.end)


# store_macro():
def test_store_macro_as_expected():
    line = 'macro WHATEVER 69 dump end'
    name = get_next_symbol(line, 5)
    store_macro(line, name.value, name.end)
    assert Builtins.BUILTIN_MACRO[name.value] == [(TokenId.INT, 69), (TokenId.OP, "dump")]

def test_store_macro_force_error_with_recursive():
    line = 'macro WHATEVER 69 dump WHATEVER end'
    name = get_next_symbol(line, 5)
    with pytest.raises(AssertionError):
        store_macro(line, name.value, name.end)


# lex_macro_from_builtins()
def test_lex_macro_from_builtins_as_expected():
    result = list(lex_macro_from_builtins('write'))
    assert result == [(OperandId.PUSH_INT, 1), (OperandId.PUSH_INT, 1), (OperandId.SYSCALL, 'syscall')]

def test_lex_macro_from_builtins_new_macro():
    line = 'macro testtest 69 dump end'
    name = get_next_symbol(line, 5)
    store_macro(line, name.value, name.end)
    result = list(lex_macro_from_builtins('testtest'))
    assert result == [(OperandId.PUSH_INT, 69), (OperandId.DUMP, 'dump')]

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


## lex_tokens_from_file
def test_lex_tokens_from_file_arithmetic_plus():
    result = lex_tokens_from_file('tests/arithmetic-plus.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/arithmetic-plus.nv', 2, 1), 34),
                      Token(TokenId.INT, FileLocation('tests/arithmetic-plus.nv', 2, 4), 35),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-plus.nv', 2, 7), '+'),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-plus.nv', 2, 9), 'dump')
                     ]

def test_lex_tokens_from_file_arithmetic_minus():
    result = lex_tokens_from_file('tests/arithmetic-minus.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/arithmetic-minus.nv', 2, 1), 500),
                      Token(TokenId.INT, FileLocation('tests/arithmetic-minus.nv', 2, 5), 80),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-minus.nv', 2, 8), '-'),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-minus.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_arithmetic_multiply():
    result = lex_tokens_from_file('tests/arithmetic-multiply.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/arithmetic-multiply.nv', 2, 1), 3),
                      Token(TokenId.INT, FileLocation('tests/arithmetic-multiply.nv', 2, 3), 23),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-multiply.nv', 2, 6), '*'),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-multiply.nv', 2, 8), 'dump')
                     ]

# TODO implement divide
def test_lex_tokens_from_file_arithmetic_divide():
    pass

# TODO implement modulo
def test_lex_tokens_from_file_arithmetic_mod():
    pass

# TODO implement tests for logical-operators
def test_lex_tokens_from_file_logical_operator_equal():
    result = lex_tokens_from_file('tests/logical-operator-equal.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-equal.nv', 2, 7), '=='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-equal.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_not_equal():
    result = lex_tokens_from_file('tests/logical-operator-not-equal.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-not-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-not-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-not-equal.nv', 2, 7), '!='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-not-equal.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_greater_than():
    result = lex_tokens_from_file('tests/logical-operator-greater-than.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than.nv', 2, 7), '>'),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than.nv', 2, 9), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_greater_than_or_equal_to():
    result = lex_tokens_from_file('tests/logical-operator-greater-than-or-equal.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 7), '>='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_less_than():
    result = lex_tokens_from_file('tests/logical-operator-less-than.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than.nv', 2, 7), '<'),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than.nv', 2, 9), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_less_than_or_equal_to():
    result = lex_tokens_from_file('tests/logical-operator-less-than-or-equal.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 7), '<='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 10), 'dump')
                     ]

# TODO implement tests for stack-operators
# TODO implement tests for bitwise-operators
# TODO implement tests for buffer-operators

def test_lex_tokens_from_file_local_macro():
    result = lex_tokens_from_file('tests/local-macro.nv')
    assert result == [
                      Token(TokenId.MACRO, FileLocation('tests/local-macro.nv', 4, 1), 'write69'),
                     ]

def test_lex_tokens_from_file_local_const():
    result = lex_tokens_from_file('tests/local-constant.nv')
    assert result == [
                      Token(TokenId.CONST, FileLocation('tests/local-constant.nv', 3, 1), 'HELLO'),
                      Token(TokenId.OP, FileLocation('tests/local-constant.nv', 3, 7), 'dump'),
                     ]



'''

def parse_tokens_from_file(input_file_path: str):
    with open(input_file_path, "r") as file:
        return [Token(typ      = token_type,
                      location = FileLocation(input_file_path, row+1, col+1),
                      value    = token_value)
                for (row, line) in enumerate(file.readlines())
                for (col, (token_type, token_value)) in parse_line(line.split("//")[0])]




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
