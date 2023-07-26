from nova.tokenizer import Tokenizer
from nova.lexer import Lexer
from nova.parser import Parser
from nova.simulator import simulate_program

# TODO implement capability to store strings in a macro
# TODO add test to /tests for simulation and compilation test
# TODO implement /tests that force errors

# simulate_program():
def test_simulate_program_arithmetic_plus(capsys):
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '69\n'

def test_simulate_program_arithmetic_minus(capsys):
    tokenizer = Tokenizer('tests/arithmetic-minus.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '420\n'

def test_simulate_program_arithmetic_multiply(capsys):
    tokenizer = Tokenizer('tests/arithmetic-multiply.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '69\n'

# TODO implement divide
def test_simulate_program_arithmetic_divide():
    pass

# TODO implement modulo
def test_simulate_program_arithmetic_mod():
    pass

def test_simulate_program_logical_operator_equal(capsys):
    tokenizer = Tokenizer('tests/logical-operator-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '1\n'

def test_simulate_program_logical_operator_not_equal(capsys):
    tokenizer = Tokenizer('tests/logical-operator-not-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '0\n'

def test_simulate_program_logical_operator_greater_than(capsys):
    tokenizer = Tokenizer('tests/logical-operator-greater-than.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '0\n'

def test_simulate_program_logical_operator_greater_than_or_equal_to(capsys):
    tokenizer = Tokenizer('tests/logical-operator-greater-than-or-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '1\n'

def test_simulate_program_logical_operator_less_than(capsys):
    tokenizer = Tokenizer('tests/logical-operator-less-than.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '0\n'

def test_simulate_program_logical_operator_less_than_or_equal_to(capsys):
    tokenizer = Tokenizer('tests/logical-operator-less-than-or-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '1\n'

def test_simulate_program_stack_operator_dump(capsys):
    tokenizer = Tokenizer('tests/stack-operator-dump.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '69\n'

def test_simulate_program_stack_operator_drop(capsys):
    tokenizer = Tokenizer('tests/stack-operator-drop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '420\n'

def test_simulate_program_stack_operator_duplicate(capsys):
    tokenizer = Tokenizer('tests/stack-operator-duplicate.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '69\n69\n'

def test_simulate_program_stack_operator_2duplicate(capsys):
    tokenizer = Tokenizer('tests/stack-operator-2duplicate.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '420\n69\n420\n69\n'

def test_simulate_program_stack_operator_swap(capsys):
    tokenizer = Tokenizer('tests/stack-operator-swap.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\n'

def test_simulate_program_stack_operator_over(capsys):
    tokenizer = Tokenizer('tests/stack-operator-over.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '69\n420\n69\n'

def test_simulate_program_bitwise_operator_and(capsys):
    tokenizer = Tokenizer('tests/bitwise-operator-and.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '2\n'

def test_simulate_program_bitwise_operator_or(capsys):
    tokenizer = Tokenizer('tests/bitwise-operator-or.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '3\n'

def test_simulate_program_bitwise_operator_shift_left(capsys):
    tokenizer = Tokenizer('tests/bitwise-operator-shift-left.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '8\n'

def test_simulate_program_bitwise_operator_shift_right(capsys):
    tokenizer = Tokenizer('tests/bitwise-operator-shift-right.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '1\n'

def test_simulate_program_conditional_if(capsys):
    tokenizer = Tokenizer('tests/conditional-if.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '420\n'

def test_simulate_program_conditional_if_else(capsys):
    tokenizer = Tokenizer('tests/conditional-if-else.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '6969\n'

def test_simulate_program_conditional_nested_if_else(capsys):
    tokenizer = Tokenizer('tests/conditional-nested-if-else.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '420\n'

def test_simulate_program_conditional_while(capsys):
    tokenizer = Tokenizer('tests/conditional-while-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n'

def test_simulate_program_conditional_nested_while_if(capsys):
    tokenizer = Tokenizer('tests/conditional-nested-while-if-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '3\n'

def test_simulate_program_conditional_nested_while(capsys):
    tokenizer = Tokenizer('tests/conditional-nested-while-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == '0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n2\n'

## TODO Add 'and'
def test_simulate_program_conditional_and():
    pass

## TODO Add 'or'
def test_simulate_program_conditional_or():
    pass

def test_simulate_program_buffer_string_literal(capsys):
    tokenizer = Tokenizer('tests/buffer-string-literal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == 'Hello, World!\nWhatcha Doing!\n'

def test_simulate_program_buffer_store_single_bytes(capsys):
    tokenizer = Tokenizer('tests/buffer-store-single-bytes.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    simulate_program(parser.program)
    captured = capsys.readouterr()
    assert captured.out == 'abc'

