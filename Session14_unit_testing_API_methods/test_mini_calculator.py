from mini_calculator import MiniCalculator

def test_addition():
    mc = MiniCalculator(3, 2)
    assert mc.addition() == 5
def test_substraction():
    mc = MiniCalculator(3, 2)
    assert mc.substraction() == 1

def test_multiplication():
    mc = MiniCalculator(3, 2)
    assert mc.multiplication() == 6

def test_division():
    mc = MiniCalculator(3, 2)
    assert mc.division() == 1.5