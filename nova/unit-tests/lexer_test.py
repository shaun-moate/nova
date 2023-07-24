import pytest
from nova.lexer import Lexer
from nova.dataclasses import FileLocation, TokenId, Token

# lex_tokens():
def test_lex_tokens_from_file_arithmetic_plus():
    lexer = Lexer('tests/arithmetic-plus.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/arithmetic-plus.nv', 2, 1), 34),
                      Token(TokenId.INT, FileLocation('tests/arithmetic-plus.nv', 2, 4), 35),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-plus.nv', 2, 7), '+'),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-plus.nv', 2, 9), 'dump')
                     ]

def test_lex_tokens_from_file_arithmetic_minus():
    lexer = Lexer('tests/arithmetic-minus.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/arithmetic-minus.nv', 2, 1), 500),
                      Token(TokenId.INT, FileLocation('tests/arithmetic-minus.nv', 2, 5), 80),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-minus.nv', 2, 8), '-'),
                      Token(TokenId.OP, FileLocation('tests/arithmetic-minus.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_arithmetic_multiply():
    lexer = Lexer('tests/arithmetic-multiply.nv')
    assert lexer.tokens == [
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

def test_lex_tokens_from_file_logical_operator_equal():
    lexer = Lexer('tests/logical-operator-equal.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-equal.nv', 2, 7), '=='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-equal.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_not_equal():
    lexer = Lexer('tests/logical-operator-not-equal.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-not-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-not-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-not-equal.nv', 2, 7), '!='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-not-equal.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_greater_than():
    lexer = Lexer('tests/logical-operator-greater-than.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than.nv', 2, 7), '>'),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than.nv', 2, 9), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_greater_than_or_equal_to():
    lexer = Lexer('tests/logical-operator-greater-than-or-equal.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 7), '>='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-greater-than-or-equal.nv', 2, 10), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_less_than():
    lexer = Lexer('tests/logical-operator-less-than.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than.nv', 2, 7), '<'),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than.nv', 2, 9), 'dump')
                     ]

def test_lex_tokens_from_file_logical_operator_less_than_or_equal_to():
    lexer = Lexer('tests/logical-operator-less-than-or-equal.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 7), '<='),
                      Token(TokenId.OP, FileLocation('tests/logical-operator-less-than-or-equal.nv', 2, 10), 'dump')
                     ]


def test_lex_tokens_from_file_stack_operator_dump():
    lexer = Lexer('tests/stack-operator-dump.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-dump.nv', 2, 1), 69),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-dump.nv', 2, 4), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_drop():
    lexer = Lexer('tests/stack-operator-drop.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-drop.nv', 2, 1), 420),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-drop.nv', 2, 5), 69),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-drop.nv', 2, 8), 'drop'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-drop.nv', 2, 13), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_duplicate():
    lexer = Lexer('tests/stack-operator-duplicate.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-duplicate.nv', 2, 1), 69),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-duplicate.nv', 2, 4), 'dup'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-duplicate.nv', 2, 8), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-duplicate.nv', 2, 13), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_2duplicate():
    lexer = Lexer('tests/stack-operator-2duplicate.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-2duplicate.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-2duplicate.nv', 2, 4), 420),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 8), '2dup'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 13), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 18), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 23), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 28), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_swap():
    lexer = Lexer('tests/stack-operator-swap.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-swap.nv', 2, 1), 1),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-swap.nv', 2, 3), 2),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-swap.nv', 2, 5), 'swap'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-swap.nv', 2, 10), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-swap.nv', 2, 15), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_over():
    lexer = Lexer('tests/stack-operator-over.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-over.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-over.nv', 2, 4), 420),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 8), 'over'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 13), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 18), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 23), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_and():
    lexer = Lexer('tests/bitwise-operator-and.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-and.nv', 2, 1), 2),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-and.nv', 2, 3), 3),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-and.nv', 2, 5), 'band'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-and.nv', 2, 10), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_or():
    lexer = Lexer('tests/bitwise-operator-or.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-or.nv', 2, 1), 2),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-or.nv', 2, 3), 3),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-or.nv', 2, 5), 'bor'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-or.nv', 2, 9), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_shift_left():
    lexer = Lexer('tests/bitwise-operator-shift-left.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 1), 1),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 3), 3),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 5), 'shl'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 9), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_shift_right():
    lexer = Lexer('tests/bitwise-operator-shift-right.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 1), 2),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 3), 1),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 5), 'shr'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 9), 'dump'),
                     ]

def test_lex_tokens_from_file_conditional_if():
    lexer = Lexer('tests/conditional-if.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/conditional-if.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/conditional-if.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 2, 7), '=='),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 2, 10), 'if'),
                      Token(TokenId.INT, FileLocation('tests/conditional-if.nv', 3, 3), 420),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 3, 7), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 4, 1), 'fi'),
                     ]

def test_lex_tokens_from_file_conditional_if_else():
    lexer = Lexer('tests/conditional-if-else.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/conditional-if-else.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/conditional-if-else.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/conditional-if-else.nv', 2, 7), '!='),
                      Token(TokenId.OP, FileLocation('tests/conditional-if-else.nv', 2, 10), 'if'),
                      Token(TokenId.INT, FileLocation('tests/conditional-if-else.nv', 3, 5), 420),
                      Token(TokenId.OP, FileLocation('tests/conditional-if-else.nv', 3, 9), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-if-else.nv', 4, 1), 'else'),
                      Token(TokenId.INT, FileLocation('tests/conditional-if-else.nv', 5, 5), 6969),
                      Token(TokenId.OP, FileLocation('tests/conditional-if-else.nv', 5, 10), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-if-else.nv', 6, 1), 'fi'),
                     ]

def test_lex_tokens_from_file_conditional_nested_if_else():
    lexer = Lexer('tests/conditional-nested-if-else.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 2, 1), 34),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 2, 4), 35),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 2, 7), '+'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 2, 9), 69),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 2, 12), '!='),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 2, 15), 'if'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 3, 4), 10),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 3, 7), 10),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 3, 10), '!='),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 3, 13), 'if'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 4, 7), 13),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 4, 10), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 5, 4), 'else'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 6, 7), 69),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 6, 10), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 7, 4), 'fi'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 8, 1), 'else'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-if-else.nv', 9, 4), 420),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 9, 8), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-if-else.nv', 10, 1), 'fi'),
                     ]

def test_lex_tokens_from_file_conditional_while():
    lexer = Lexer('tests/conditional-while-loop.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/conditional-while-loop.nv', 2, 1), 69),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 3, 1), 'while'),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 3, 7), 'dup'),
                      Token(TokenId.INT, FileLocation('tests/conditional-while-loop.nv', 3, 11), 0),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 3, 13), '>'),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 3, 15), 'do'),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 4, 4), 'dup'),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 4, 8), 'dump'),
                      Token(TokenId.INT, FileLocation('tests/conditional-while-loop.nv', 5, 4), 1),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 5, 6), '-'),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 6, 1), 'done'),
                      Token(TokenId.OP, FileLocation('tests/conditional-while-loop.nv', 7, 1), 'drop'),
                     ]

def test_lex_tokens_from_file_conditional_nested_while_if():
    lexer = Lexer('tests/conditional-nested-while-if-loop.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 1), 0),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 3), 'while'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 9), 'dup'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 13), 5),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 15), '<='),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 2, 18), 'do'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 4), 'dup'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 8), 3),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 10), '=='),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 3, 13), 'if'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 4, 7), 'dup'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 4, 11), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 5, 4), 'fi'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-if-loop.nv', 6, 4), 1),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 6, 6), '+'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 7, 1), 'done'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-if-loop.nv', 7, 6), 'drop'),
                     ]

def test_lex_tokens_from_file_conditional_nested_while():
    lexer = Lexer('tests/conditional-nested-while-loop.nv')
    assert lexer.tokens == [
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-loop.nv', 2, 1), 0),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 2, 3), 'while'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 2, 9), 'dup'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-loop.nv', 2, 13), 5),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 2, 15), '<'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 2, 17), 'do'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-loop.nv', 3, 3), 0),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 3, 5), 'while'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 3, 11), 'dup'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-loop.nv', 3, 15), 3),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 3, 17), '<'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 3, 19), 'do'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 4, 5), 'dup'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 4, 9), 'dump'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-loop.nv', 5, 5), 1),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 5, 7), '+'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 6, 3), 'done'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 6, 8), 'drop'),
                      Token(TokenId.INT, FileLocation('tests/conditional-nested-while-loop.nv', 7, 3), 1),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 7, 5), '+'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 8, 1), 'done'),
                      Token(TokenId.OP, FileLocation('tests/conditional-nested-while-loop.nv', 8, 6), 'drop'),
                     ]

## TODO Add 'and'
def test_lex_tokens_from_file_conditional_and():
    pass

## TODO Add 'or'
def test_lex_tokens_from_file_conditional_or():
    pass

def test_lex_tokens_from_file_local_macro():
    lexer = Lexer('tests/local-macro.nv')
    assert lexer.tokens == [
                      Token(TokenId.MACRO, FileLocation('tests/local-macro.nv', 4, 1), 'write69'),
                     ]

def test_lex_tokens_from_file_local_const():
    lexer = Lexer('tests/local-constant.nv')
    assert lexer.tokens == [
                      Token(TokenId.CONST, FileLocation('tests/local-constant.nv', 3, 1), 'HELLO'),
                      Token(TokenId.OP, FileLocation('tests/local-constant.nv', 3, 7), 'dump'),
                     ]

def test_lex_tokens_from_file_buffer_string_literal():
    lexer = Lexer('tests/buffer-string-literal.nv')
    assert lexer.tokens == [
                      Token(TokenId.STR, FileLocation('tests/buffer-string-literal.nv', 1, 1), 'Hello, World!\n'),
                      Token(TokenId.MACRO, FileLocation('tests/buffer-string-literal.nv', 1, 19), 'write'),
                      Token(TokenId.STR, FileLocation('tests/buffer-string-literal.nv', 2, 1), 'Whatcha Doing!\n'),
                      Token(TokenId.MACRO, FileLocation('tests/buffer-string-literal.nv', 2, 20), 'write'),
                     ]

def test_lex_tokens_from_file_buffer_store_single_bytes():
    lexer = Lexer('tests/buffer-store-single-bytes.nv')
    assert lexer.tokens == [
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 2, 1), 'mem'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 2, 5), 0),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 2, 7), '+'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 2, 9), 97),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 2, 12), 'store8'),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 3, 1), 'mem'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 3, 5), 1),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 3, 7), '+'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 3, 9), 98),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 3, 12), 'store8'),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 4, 1), 'mem'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 4, 5), 2),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 4, 7), '+'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 4, 9), 99),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 4, 12), 'store8'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 5, 1), 3),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 5, 3), 'mem'),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 5, 7), 1),
                      Token(TokenId.INT, FileLocation('tests/buffer-store-single-bytes.nv', 5, 9), 1),
                      Token(TokenId.OP, FileLocation('tests/buffer-store-single-bytes.nv', 5, 11), 'syscall'),
                     ]

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


# assign_token_type
def test_check_assign_token_type_str():
    lexer = Lexer('tests/arithmetic-plus.nv')
    token = lexer.assign_token_type(token="forty-two", typ="str")
    assert token == (TokenId.STR, "forty-two")

def test_check_assign_token_type_macro():
    lexer = Lexer('tests/arithmetic-plus.nv')
    token = lexer.assign_token_type(token="forty-two", typ="macro")
    assert token == (TokenId.MACRO, "forty-two")

def test_check_assign_token_type_const():
    lexer = Lexer('tests/arithmetic-plus.nv')
    token = lexer.assign_token_type(token="forty-two", typ="const")
    assert token == (TokenId.CONST, "forty-two")

def test_check_assign_token_type_int():
    lexer = Lexer('tests/arithmetic-plus.nv')
    token = lexer.assign_token_type(token="42", typ="int")
    assert token == (TokenId.INT, 42)

def test_check_assign_token_type_int_string_passed_error():
    lexer = Lexer('tests/arithmetic-plus.nv')
    with pytest.raises(AssertionError):
        lexer.assign_token_type(token="forty-two", typ="int")

def test_check_assign_token_type_operand():
    lexer = Lexer('tests/arithmetic-plus.nv')
    token = lexer.assign_token_type(token="forty-two", typ="op")
    assert token == (TokenId.OP, "forty-two")
