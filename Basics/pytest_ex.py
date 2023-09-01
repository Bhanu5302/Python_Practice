"""The assert keyword is used when debugging code.
 The assert keyword lets you test if a condition in your code returns True,
if not, the program will raise an AssertionError"""

import math_func

def test_add():
    assert math_func.add(3, 3) == 6
    assert math_func.add(3) == 5
    assert math_func.add(2) == 4

def test_product():
    assert math_func.product(2, 3) == 6

    assert math_func.product(2, 2) == 4