from nova.builtins import OperandId

def test_check_exhaustive_list_operand_ids():
    assert len(OperandId) == 33
