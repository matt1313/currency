from currency import Currency

def test_two_currencies():
    a = Currency('USD', 8)
    b = Currency('USD', 8)
    assert a == b

def test_two_diff_currencies():
    a = Currency('USD', 6)
    b = Currency('Euro', 4)
    assert a!=b
