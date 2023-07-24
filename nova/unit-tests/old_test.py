import pytest

from nova.old import *
from nova.builtins import *
from nova.helpers import *
from nova.dataclasses import *


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


def test_lex_tokens_from_file_stack_operator_dump():
    result = lex_tokens_from_file('tests/stack-operator-dump.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-dump.nv', 2, 1), 69),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-dump.nv', 2, 4), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_drop():
    result = lex_tokens_from_file('tests/stack-operator-drop.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-drop.nv', 2, 1), 420),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-drop.nv', 2, 5), 69),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-drop.nv', 2, 8), 'drop'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-drop.nv', 2, 13), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_duplicate():
    result = lex_tokens_from_file('tests/stack-operator-duplicate.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-duplicate.nv', 2, 1), 69),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-duplicate.nv', 2, 4), 'dup'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-duplicate.nv', 2, 8), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-duplicate.nv', 2, 13), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_2duplicate():
    result = lex_tokens_from_file('tests/stack-operator-2duplicate.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-2duplicate.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-2duplicate.nv', 2, 4), 420),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 8), '2dup'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 13), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 18), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 23), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-2duplicate.nv', 2, 28), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_swap():
    result = lex_tokens_from_file('tests/stack-operator-swap.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-swap.nv', 2, 1), 1),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-swap.nv', 2, 3), 2),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-swap.nv', 2, 5), 'swap'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-swap.nv', 2, 10), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-swap.nv', 2, 15), 'dump'),
                     ]

def test_lex_tokens_from_file_stack_operator_over():
    result = lex_tokens_from_file('tests/stack-operator-over.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/stack-operator-over.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/stack-operator-over.nv', 2, 4), 420),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 8), 'over'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 13), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 18), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/stack-operator-over.nv', 2, 23), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_and():
    result = lex_tokens_from_file('tests/bitwise-operator-and.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-and.nv', 2, 1), 2),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-and.nv', 2, 3), 3),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-and.nv', 2, 5), 'band'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-and.nv', 2, 10), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_or():
    result = lex_tokens_from_file('tests/bitwise-operator-or.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-or.nv', 2, 1), 2),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-or.nv', 2, 3), 3),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-or.nv', 2, 5), 'bor'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-or.nv', 2, 9), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_shift_left():
    result = lex_tokens_from_file('tests/bitwise-operator-shift-left.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 1), 1),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 3), 3),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 5), 'shl'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-left.nv', 2, 9), 'dump'),
                     ]

def test_lex_tokens_from_file_bitwise_operator_shift_right():
    result = lex_tokens_from_file('tests/bitwise-operator-shift-right.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 1), 2),
                      Token(TokenId.INT, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 3), 1),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 5), 'shr'),
                      Token(TokenId.OP, FileLocation('tests/bitwise-operator-shift-right.nv', 2, 9), 'dump'),
                     ]

def test_lex_tokens_from_file_buffer_string_literal():
    result = lex_tokens_from_file('tests/buffer-string-literal.nv')
    assert result == [
                      Token(TokenId.STR, FileLocation('tests/buffer-string-literal.nv', 1, 1), 'Hello, World!\n'),
                      Token(TokenId.MACRO, FileLocation('tests/buffer-string-literal.nv', 1, 19), 'write'),
                      Token(TokenId.STR, FileLocation('tests/buffer-string-literal.nv', 2, 1), 'Whatcha Doing!\n'),
                      Token(TokenId.MACRO, FileLocation('tests/buffer-string-literal.nv', 2, 20), 'write'),
                     ]

def test_lex_tokens_from_file_buffer_store_single_bytes():
    result = lex_tokens_from_file('tests/buffer-store-single-bytes.nv')
    assert result == [
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

def test_lex_tokens_from_file_conditional_if():
    result = lex_tokens_from_file('tests/conditional-if.nv')
    assert result == [
                      Token(TokenId.INT, FileLocation('tests/conditional-if.nv', 2, 1), 69),
                      Token(TokenId.INT, FileLocation('tests/conditional-if.nv', 2, 4), 69),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 2, 7), '=='),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 2, 10), 'if'),
                      Token(TokenId.INT, FileLocation('tests/conditional-if.nv', 3, 3), 420),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 3, 7), 'dump'),
                      Token(TokenId.OP, FileLocation('tests/conditional-if.nv', 4, 1), 'fi'),
                     ]

def test_lex_tokens_from_file_conditional_if_else():
    result = lex_tokens_from_file('tests/conditional-if-else.nv')
    assert result == [
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
    result = lex_tokens_from_file('tests/conditional-nested-if-else.nv')
    assert result == [
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
    result = lex_tokens_from_file('tests/conditional-while-loop.nv')
    assert result == [
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
    result = lex_tokens_from_file('tests/conditional-nested-while-if-loop.nv')
    assert result == [
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
    result = lex_tokens_from_file('tests/conditional-nested-while-loop.nv')
    assert result == [
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
