from nova.parser import Parser
from nova.dataclasses import OperandId

# lex_macro_from_builtins()
def test_lex_macro_from_builtins_as_expected():
    pass
    # result = list(lex_macro_from_builtins('write'))
    # assert result == [(OperandId.PUSH_INT, 1), (OperandId.PUSH_INT, 1), (OperandId.SYSCALL, 'syscall')]

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
