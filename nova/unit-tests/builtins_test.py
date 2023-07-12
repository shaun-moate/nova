from nova.builtins import *

def test_check_for_exhaustive_list_operands():
    assert len(Builtins.BUILTIN_OPS) == 33

def test_check_for_exhaustive_list_macros():
    assert len(Builtins.BUILTIN_MACRO) == 1

def test_check_for_exhaustive_list_consts():
    assert len(Builtins.BUILTIN_CONST) == 1

def test_check_exhaustive_list_operand_ids():
    assert len(OperandId) == 33

def test_check_exhaustive_list_macro_ids():
    assert len(MacroId) == 1

def test_check_exhaustive_list_token_ids():
    assert len(TokenId) == 5

def test_check_exhaustive_list_constant_ids():
    assert len(ConstantId) == 1
