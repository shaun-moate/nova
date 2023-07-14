from nova.builtins import *

## Token Type
def test_check_exhaustive_list_token_ids():
    assert len(TokenId) == 5


## Operators
def test_check_for_exhaustive_list_operands():
    assert len(Builtins.BUILTIN_OPS) == 33

def test_check_exhaustive_list_operand_ids():
    assert len(OperandId) == 33

def test_check_for_unreachable_operand():
    assert not Builtins.BUILTIN_OPS == "forty-two"

def test_check_is_string_operand():
    assert not Builtins.BUILTIN_OPS == 42


## Macros
def test_check_for_exhaustive_list_macros():
    assert len(Builtins.BUILTIN_MACRO) == 1

def test_check_exhaustive_list_macro_ids():
    assert len(MacroId) == 1

def test_check_for_unreachable_macro():
    assert not Builtins.BUILTIN_MACRO == "forty-two"

def test_check_is_string_macro():
    assert not Builtins.BUILTIN_MACRO == 42


## Constants
def test_check_for_exhaustive_list_consts():
    assert len(Builtins.BUILTIN_CONST) == 1

def test_check_exhaustive_list_constant_ids():
    assert len(ConstantId) == 1

def test_check_for_unreachable_constant():
    assert not Builtins.BUILTIN_CONST == "forty-two"

def test_check_is_string_constant():
    assert not Builtins.BUILTIN_CONST == 42


