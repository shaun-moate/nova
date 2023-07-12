from nova.builtins import Builtins

def test_check_for_exhaustive_list_operands():
    assert len(Builtins.BUILTIN_OPS) == 33

def test_check_for_exhaustive_list_macros():
    assert len(Builtins.BUILTIN_MACRO) == 1

def test_check_for_exhaustive_list_consts():
    assert len(Builtins.BUILTIN_CONST) == 1
