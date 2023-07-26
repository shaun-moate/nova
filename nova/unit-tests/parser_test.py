from nova.tokenizer import Tokenizer
from nova.lexer import Lexer
from nova.parser import Parser
from nova.dataclasses import FileLocation, OperandId, Operand, Program

# TODO implement capability to store strings in a macro
# TODO add test to /tests for simulation and compilation test
# TODO implement /tests that force errors

# generate_program():
def test_generate_program_arithmetic_plus():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/arithmetic-plus.nv', 2, 1), 34),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/arithmetic-plus.nv', 2, 4), 35), 
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/arithmetic-plus.nv', 2, 7), '+'), 
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/arithmetic-plus.nv', 2, 9), 'dump'),
                      ])

def test_generate_program_arithmetic_minus():
    tokenizer = Tokenizer('tests/arithmetic-minus.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/arithmetic-minus.nv', 2, 1), 500),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/arithmetic-minus.nv', 2, 5), 80), 
                      Operand(OperandId.MINUS, -1, -1, FileLocation('tests/arithmetic-minus.nv', 2, 8), '-'), 
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/arithmetic-minus.nv', 2, 10), 'dump'),
                      ])

def test_generate_program_arithmetic_multiply():
    tokenizer = Tokenizer('tests/arithmetic-multiply.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/arithmetic-multiply.nv', 2, 1), 3),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/arithmetic-multiply.nv', 2, 3), 23), 
                      Operand(OperandId.MULT, -1, -1, FileLocation('tests/arithmetic-multiply.nv', 2, 6), '*'), 
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/arithmetic-multiply.nv', 2, 8), 'dump'),
                      ])

# TODO implement divide
def test_generate_program_arithmetic_divide():
    pass

# TODO implement modulo
def test_generate_program_arithmetic_mod():
    pass

def test_generate_program_logical_operator_equal():
    tokenizer = Tokenizer('tests/logical-operator-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-equal.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-equal.nv', 2, 4), 69),
                      Operand(OperandId.EQUAL, -1, -1, FileLocation('tests/logical-operator-equal.nv', 2, 7), '=='),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/logical-operator-equal.nv', 2, 10), 'dump')
                     ])

def test_generate_program_logical_operator_not_equal():
    tokenizer = Tokenizer('tests/logical-operator-not-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-not-equal.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-not-equal.nv', 2, 4), 69),
                      Operand(OperandId.NOT_EQUAL, -1, -1, FileLocation('tests/logical-operator-not-equal.nv', 2, 7), '!='),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/logical-operator-not-equal.nv', 2, 10), 'dump')
                     ])

def test_generate_program_logical_operator_greater_than():
    tokenizer = Tokenizer('tests/logical-operator-greater-than.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-greater-than.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-greater-than.nv', 2, 4), 69),
                      Operand(OperandId.GREATER, -1, -1, FileLocation('tests/logical-operator-greater-than.nv', 2, 7), '>'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/logical-operator-greater-than.nv', 2, 9), 'dump')
                     ])

def test_generate_program_logical_operator_greater_than_or_equal_to():
    tokenizer = Tokenizer('tests/logical-operator-greater-than-or-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 4), 69),
                      Operand(OperandId.GR_EQ, -1, -1, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 7), '>='),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 10), 'dump')
                     ])

def test_generate_program_logical_operator_less_than():
    tokenizer = Tokenizer('tests/logical-operator-less-than.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-less-than.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-less-than.nv', 2, 4), 69),
                      Operand(OperandId.LESSER, -1, -1, FileLocation('tests/logical-operator-less-than.nv', 2, 7), '<'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/logical-operator-less-than.nv', 2, 9), 'dump')
                     ])

def test_generate_program_logical_operator_less_than_or_equal_to():
    tokenizer = Tokenizer('tests/logical-operator-less-than-or-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 4), 69),
                      Operand(OperandId.LESS_EQ, -1, -1, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 7), '<='),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 10), 'dump')
                     ])

def test_generate_program_stack_operator_dump():
    tokenizer = Tokenizer('tests/stack-operator-dump.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-dump.nv', 2, 1), 69),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-dump.nv', 2, 4), 'dump'),
                     ])

def test_generate_program_stack_operator_drop():
    tokenizer = Tokenizer('tests/stack-operator-drop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-drop.nv', 2, 1), 420),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-drop.nv', 2, 5), 69),
                      Operand(OperandId.DROP, -1, -1, FileLocation('tests/stack-operator-drop.nv', 2, 8), 'drop'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-drop.nv', 2, 13), 'dump'),
                     ])

def test_generate_program_stack_operator_duplicate():
    tokenizer = Tokenizer('tests/stack-operator-duplicate.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-duplicate.nv', 2, 1), 69),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/stack-operator-duplicate.nv', 2, 4), 'dup'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-duplicate.nv', 2, 8), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-duplicate.nv', 2, 13), 'dump'),
                     ])

def test_generate_program_stack_operator_2duplicate():
    tokenizer = Tokenizer('tests/stack-operator-2duplicate.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 4), 420),
                      Operand(OperandId.DUP2, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 8), '2dup'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 13), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 18), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 23), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-2duplicate.nv', 2, 28), 'dump'),
                     ])

def test_generate_program_stack_operator_swap():
    tokenizer = Tokenizer('tests/stack-operator-swap.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-swap.nv', 2, 1), 1),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-swap.nv', 2, 3), 2),
                      Operand(OperandId.SWAP, -1, -1, FileLocation('tests/stack-operator-swap.nv', 2, 5), 'swap'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-swap.nv', 2, 10), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-swap.nv', 2, 15), 'dump'),
                     ])

def test_generate_program_stack_operator_over():
    tokenizer = Tokenizer('tests/stack-operator-over.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-over.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/stack-operator-over.nv', 2, 4), 420),
                      Operand(OperandId.OVER, -1, -1, FileLocation('tests/stack-operator-over.nv', 2, 8), 'over'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-over.nv', 2, 13), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-over.nv', 2, 18), 'dump'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/stack-operator-over.nv', 2, 23), 'dump'),
                     ])

def test_generate_program_bitwise_operator_and():
    tokenizer = Tokenizer('tests/bitwise-operator-and.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-and.nv', 2, 1), 2),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-and.nv', 2, 3), 3),
                      Operand(OperandId.BAND, -1, -1, FileLocation('tests/bitwise-operator-and.nv', 2, 5), 'band'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/bitwise-operator-and.nv', 2, 10), 'dump'),
                     ])

def test_generate_program_bitwise_operator_or():
    tokenizer = Tokenizer('tests/bitwise-operator-or.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-or.nv', 2, 1), 2),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-or.nv', 2, 3), 3),
                      Operand(OperandId.BOR, -1, -1, FileLocation('tests/bitwise-operator-or.nv', 2, 5), 'bor'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/bitwise-operator-or.nv', 2, 9), 'dump'),
                     ])

def test_generate_program_bitwise_operator_shift_left():
    tokenizer = Tokenizer('tests/bitwise-operator-shift-left.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 1), 1),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 3), 3),
                      Operand(OperandId.SHL, -1, -1, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 5), 'shl'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 9), 'dump'),
                     ])

def test_generate_program_bitwise_operator_shift_right():
    tokenizer = Tokenizer('tests/bitwise-operator-shift-right.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 1), 2),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 3), 1),
                      Operand(OperandId.SHR, -1, -1, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 5), 'shr'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 9), 'dump'),
                     ])

def test_generate_program_conditional_if():
    tokenizer = Tokenizer('tests/conditional-if.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if.nv', 2, 4), 69),
                      Operand(OperandId.EQUAL, -1, -1, FileLocation('tests/conditional-if.nv', 2, 7), '=='),
                      Operand(OperandId.IF, 6, -1, FileLocation('tests/conditional-if.nv', 2, 10), 'if'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if.nv', 3, 3), 420),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-if.nv', 3, 7), 'dump'),
                      Operand(OperandId.FI, 7, -1, FileLocation('tests/conditional-if.nv', 4, 1), 'fi'),
                     ])

def test_generate_program_conditional_if_else():
    tokenizer = Tokenizer('tests/conditional-if-else.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if-else.nv', 2, 1), 69),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if-else.nv', 2, 4), 69),
                      Operand(OperandId.NOT_EQUAL, -1, -1, FileLocation('tests/conditional-if-else.nv', 2, 7), '!='),
                      Operand(OperandId.IF, 7, -1, FileLocation('tests/conditional-if-else.nv', 2, 10), 'if'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if-else.nv', 3, 5), 420),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-if-else.nv', 3, 9), 'dump'),
                      Operand(OperandId.ELSE, 9, -1, FileLocation('tests/conditional-if-else.nv', 4, 1), 'else'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-if-else.nv', 5, 5), 6969),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-if-else.nv', 5, 10), 'dump'),
                      Operand(OperandId.FI, 10, -1, FileLocation('tests/conditional-if-else.nv', 6, 1), 'fi'),
                     ])

def test_generate_program_conditional_nested_if_else():
    tokenizer = Tokenizer('tests/conditional-nested-if-else.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 2, 1), 34),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 2, 4), 35),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 2, 7), '+'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 2, 9), 69),
                      Operand(OperandId.NOT_EQUAL, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 2, 12), '!='),
                      Operand(OperandId.IF, 17, -1, FileLocation('tests/conditional-nested-if-else.nv', 2, 15), 'if'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 3, 4), 10),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 3, 7), 10),
                      Operand(OperandId.NOT_EQUAL, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 3, 10), '!='),
                      Operand(OperandId.IF, 13, -1, FileLocation('tests/conditional-nested-if-else.nv', 3, 13), 'if'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 4, 7), 13),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 4, 10), 'dump'),
                      Operand(OperandId.ELSE, 15, -1, FileLocation('tests/conditional-nested-if-else.nv', 5, 4), 'else'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 6, 7), 69),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 6, 10), 'dump'),
                      Operand(OperandId.FI, 16, -1, FileLocation('tests/conditional-nested-if-else.nv', 7, 4), 'fi'),
                      Operand(OperandId.ELSE, 19, -1, FileLocation('tests/conditional-nested-if-else.nv', 8, 1), 'else'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 9, 4), 420),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-nested-if-else.nv', 9, 8), 'dump'),
                      Operand(OperandId.FI, 20, -1, FileLocation('tests/conditional-nested-if-else.nv', 10, 1), 'fi'),
                     ])

def test_generate_program_conditional_while():
    tokenizer = Tokenizer('tests/conditional-while-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-while-loop.nv', 2, 1), 69),
                      Operand(OperandId.WHILE, -1, -1, FileLocation('tests/conditional-while-loop.nv', 3, 1), 'while'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-while-loop.nv', 3, 7), 'dup'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-while-loop.nv', 3, 11), 0),
                      Operand(OperandId.GREATER, -1, -1, FileLocation('tests/conditional-while-loop.nv', 3, 13), '>'),
                      Operand(OperandId.DO, 11, -1, FileLocation('tests/conditional-while-loop.nv', 3, 15), 'do'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-while-loop.nv', 4, 4), 'dup'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-while-loop.nv', 4, 8), 'dump'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-while-loop.nv', 5, 4), 1),
                      Operand(OperandId.MINUS, -1, -1, FileLocation('tests/conditional-while-loop.nv', 5, 6), '-'),
                      Operand(OperandId.DONE, 1, -1, FileLocation('tests/conditional-while-loop.nv', 6, 1), 'done'),
                      Operand(OperandId.DROP, -1, -1, FileLocation('tests/conditional-while-loop.nv', 7, 1), 'drop'),
                     ])

def test_generate_program_conditional_nested_while_if():
    tokenizer = Tokenizer('tests/conditional-nested-while-if-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 1), 0),
                      Operand(OperandId.WHILE, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 3), 'while'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 9), 'dup'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 13), 5),
                      Operand(OperandId.LESS_EQ, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 15), '<='),
                      Operand(OperandId.DO, 16, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 18), 'do'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 4), 'dup'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 8), 3),
                      Operand(OperandId.EQUAL, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 10), '=='),
                      Operand(OperandId.IF, 12, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 13), 'if'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 4, 7), 'dup'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 4, 11), 'dump'),
                      Operand(OperandId.FI, 13, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 5, 4), 'fi'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 6, 4), 1),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 6, 6), '+'),
                      Operand(OperandId.DONE, 1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 7, 1), 'done'),
                      Operand(OperandId.DROP, -1, -1, FileLocation('tests/conditional-nested-while-if-loop.nv', 7, 6), 'drop'),
                     ])

def test_generate_program_conditional_nested_while():
    tokenizer = Tokenizer('tests/conditional-nested-while-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 2, 1), 0),
                      Operand(OperandId.WHILE, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 2, 3), 'while'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 2, 9), 'dup'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 2, 13), 5),
                      Operand(OperandId.LESSER, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 2, 15), '<'),
                      Operand(OperandId.DO, 21, -1, FileLocation('tests/conditional-nested-while-loop.nv', 2, 17), 'do'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 3, 3), 0),
                      Operand(OperandId.WHILE, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 3, 5), 'while'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 3, 11), 'dup'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 3, 15), 3),
                      Operand(OperandId.LESSER, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 3, 17), '<'),
                      Operand(OperandId.DO, 17, -1, FileLocation('tests/conditional-nested-while-loop.nv', 3, 19), 'do'),
                      Operand(OperandId.DUP, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 4, 5), 'dup'),
                      Operand(OperandId.DUMP, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 4, 9), 'dump'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 5, 5), 1),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 5, 7), '+'),
                      Operand(OperandId.DONE, 7, -1, FileLocation('tests/conditional-nested-while-loop.nv', 6, 3), 'done'),
                      Operand(OperandId.DROP, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 6, 8), 'drop'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 7, 3), 1),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 7, 5), '+'),
                      Operand(OperandId.DONE, 1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 8, 1), 'done'),
                      Operand(OperandId.DROP, -1, -1, FileLocation('tests/conditional-nested-while-loop.nv', 8, 6), 'drop'),
                     ])

## TODO Add 'and'
def test_generate_program_conditional_and():
    pass

## TODO Add 'or'
def test_generate_program_conditional_or():
    pass

def test_generate_program_buffer_string_literal():
    tokenizer = Tokenizer('tests/buffer-string-literal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.PUSH_STR, -1, -1, FileLocation('tests/buffer-string-literal.nv', 1, 1), 'Hello, World!\n'), 
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-string-literal.nv', 1, 19), 1), 
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-string-literal.nv', 1, 19), 1), 
                      Operand(OperandId.SYSCALL, -1, -1, FileLocation('tests/buffer-string-literal.nv', 1, 19), 'syscall'), 
                      Operand(OperandId.PUSH_STR, -1, -1, FileLocation('tests/buffer-string-literal.nv', 2, 1), 'Whatcha Doing!\n'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-string-literal.nv', 2, 20), 1), 
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-string-literal.nv', 2, 20), 1), 
                      Operand(OperandId.SYSCALL, -1, -1, FileLocation('tests/buffer-string-literal.nv', 2, 20), 'syscall'),
                     ])

def test_generate_program_buffer_store_single_bytes():
    tokenizer = Tokenizer('tests/buffer-store-single-bytes.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    assert parser.program == Program([
                      Operand(OperandId.MEM_ADDR, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 2, 1), 'mem'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 2, 5), 0),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 2, 7), '+'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 2, 9), 97),
                      Operand(OperandId.MEM_STORE, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 2, 12), 'store8'),
                      Operand(OperandId.MEM_ADDR, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 3, 1), 'mem'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 3, 5), 1),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 3, 7), '+'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 3, 9), 98),
                      Operand(OperandId.MEM_STORE, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 3, 12), 'store8'),
                      Operand(OperandId.MEM_ADDR, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 4, 1), 'mem'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 4, 5), 2),
                      Operand(OperandId.PLUS, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 4, 7), '+'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 4, 9), 99),
                      Operand(OperandId.MEM_STORE, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 4, 12), 'store8'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 5, 1), 3),
                      Operand(OperandId.MEM_ADDR, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 5, 3), 'mem'),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 5, 7), 1),
                      Operand(OperandId.PUSH_INT, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 5, 9), 1),
                      Operand(OperandId.SYSCALL, -1, -1, FileLocation('tests/buffer-store-single-bytes.nv', 5, 11), 'syscall'),
                     ])

# TODO add to tests error forcing examples
# def test_lex_line_to_tokens_with_unknown_op_error():
#     line = '69 96 + unknown'
#     with pytest.raises(AssertionError):
#         list(lex_line_to_tokens(line))

# def test_lex_line_to_tokens_with_new_macro():
#     line = 'macro write669 69 dump end'
#     tokens = list(lex_line_to_tokens(line))
#     assert tokens == []

# def test_lex_line_to_tokens_with_existing_macro_error():
#     line = 'macro write 42 dump end'
#     with pytest.raises(AssertionError):
#         list(lex_line_to_tokens(line))

# def test_lex_line_to_tokens_with_set_force_recursive_error():
#     line = 'macro write42 42 dump write42 end'
#     with pytest.raises(AssertionError):
#         list(lex_line_to_tokens(line))

# def test_lex_line_to_tokens_with_set_force_without_end_error():
#     line = 'macro write412 412 dump'
#     with pytest.raises(AssertionError):
#         list(lex_line_to_tokens(line))

# def test_lex_line_to_tokens_with_existing_const_error():
#     line = 'const CATCH 69'
#     with pytest.raises(AssertionError):
#         list(lex_line_to_tokens(line))

# def test_lex_line_to_tokens_with_set_const_force_must_be_integer_error():
#     line = 'const FORTY2 FORTY2'
#     with pytest.raises(AssertionError):
#         list(lex_line_to_tokens(line))

