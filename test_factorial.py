from factorial import factorial

def test_zero():
    assert factorial(0) == 0

def test_one():
    assert factorial(1) == 1

def test_two():
    assert factorial(2) == 2

def test_five():
    assert factorial(5) == 120

def test_fail():
    assert factorial(10) == 10
