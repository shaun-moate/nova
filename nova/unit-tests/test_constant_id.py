from nova.builtins import ConstantId

def test_check_exhaustive_list_constant_ids():
    assert len(ConstantId) == 1


