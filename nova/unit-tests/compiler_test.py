import subprocess
from nova.tokenizer import Tokenizer
from nova.lexer import Lexer
from nova.parser import Parser
from nova.compiler import compile_program

# TODO implement capability to store strings in a macro
# TODO add test to /tests for simulation and compilation test
# TODO implement /tests that force errors

# compile_program():
def test_compile_program_arithmetic_plus():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '69\n'

def test_compile_program_arithmetic_minus():
    tokenizer = Tokenizer('tests/arithmetic-minus.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '420\n'

def test_compile_program_arithmetic_multiply():
    tokenizer = Tokenizer('tests/arithmetic-multiply.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '69\n'

# TODO implement divide
def test_compile_program_arithmetic_divide():
    pass

# TODO implement modulo
def test_compile_program_arithmetic_mod():
    pass

def test_compile_program_logical_operator_equal():
    tokenizer = Tokenizer('tests/logical-operator-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '1\n'

def test_compile_program_logical_operator_not_equal():
    tokenizer = Tokenizer('tests/logical-operator-not-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '0\n'

def test_compile_program_logical_operator_greater_than():
    tokenizer = Tokenizer('tests/logical-operator-greater-than.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '0\n'

def test_compile_program_logical_operator_greater_than_or_equal_to():
    tokenizer = Tokenizer('tests/logical-operator-greater-than-or-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '1\n'

def test_compile_program_logical_operator_less_than():
    tokenizer = Tokenizer('tests/logical-operator-less-than.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '0\n'

def test_compile_program_logical_operator_less_than_or_equal_to():
    tokenizer = Tokenizer('tests/logical-operator-less-than-or-equal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '1\n'

def test_compile_program_stack_operator_dump():
    tokenizer = Tokenizer('tests/stack-operator-dump.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '69\n'

def test_compile_program_stack_operator_drop():
    tokenizer = Tokenizer('tests/stack-operator-drop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '420\n'

def test_compile_program_stack_operator_duplicate():
    tokenizer = Tokenizer('tests/stack-operator-duplicate.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '69\n69\n'

def test_compile_program_stack_operator_2duplicate():
    tokenizer = Tokenizer('tests/stack-operator-2duplicate.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '420\n69\n420\n69\n'

def test_compile_program_stack_operator_swap():
    tokenizer = Tokenizer('tests/stack-operator-swap.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '1\n2\n'

def test_compile_program_stack_operator_over():
    tokenizer = Tokenizer('tests/stack-operator-over.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '69\n420\n69\n'

def test_compile_program_bitwise_operator_and():
    tokenizer = Tokenizer('tests/bitwise-operator-and.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '2\n'

def test_compile_program_bitwise_operator_or():
    tokenizer = Tokenizer('tests/bitwise-operator-or.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '3\n'

def test_compile_program_bitwise_operator_shift_left():
    tokenizer = Tokenizer('tests/bitwise-operator-shift-left.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '8\n'

def test_compile_program_bitwise_operator_shift_right():
    tokenizer = Tokenizer('tests/bitwise-operator-shift-right.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '1\n'

def test_compile_program_conditional_if():
    tokenizer = Tokenizer('tests/conditional-if.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '420\n'

def test_compile_program_conditional_if_else():
    tokenizer = Tokenizer('tests/conditional-if-else.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '6969\n'

def test_compile_program_conditional_nested_if_else():
    tokenizer = Tokenizer('tests/conditional-nested-if-else.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '420\n'

def test_compile_program_conditional_while():
    tokenizer = Tokenizer('tests/conditional-while-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n'

def test_compile_program_conditional_nested_while_if():
    tokenizer = Tokenizer('tests/conditional-nested-while-if-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '3\n'

def test_compile_program_conditional_nested_while():
    tokenizer = Tokenizer('tests/conditional-nested-while-loop.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == '0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n2\n0\n1\n2\n'

## TODO Add 'and'
def test_compile_program_conditional_and():
    pass

## TODO Add 'or'
def test_compile_program_conditional_or():
    pass

def test_compile_program_buffer_string_literal():
    tokenizer = Tokenizer('tests/buffer-string-literal.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == 'Hello, World!\nWhatcha Doing!\n'

def test_compile_program_buffer_store_single_bytes():
    tokenizer = Tokenizer('tests/buffer-store-single-bytes.nv')
    lexer = Lexer(tokenizer.raw_tokens)
    parser = Parser(lexer.tokens)
    compile_program(parser.program)
    captured = subprocess.run(["build/output"], capture_output = True, text = True)
    assert captured.stdout == 'abc'


