from calcul import addition, subtraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(1, 1) == 0
    assert subtraction(0, 0) == 0

def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 0) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(1, 1) == 1
    assert division(0, 1) == 0