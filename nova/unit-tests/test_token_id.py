from nova.builtins import TokenId

def test_check_exhaustive_list_token_ids():
    assert len(TokenId) == 5

