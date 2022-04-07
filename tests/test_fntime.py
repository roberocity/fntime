from ..fntime import time_function

def fun(x):
    return x + 1

def test_time_function():
    count, name, duration, value = time_function(0.25, fun, 3)
    assert count > 1
    assert name == 'fun'
    assert duration >= 0.25
    assert value == 4

def test_time_function_with_name_specified():
    _, name, _, _ = time_function(0.1, fun, 3, method_name='testing')
    assert name == 'testing'

def test_time_with_lambda():
    fn = lambda a, b: a + b

    _, name, _, value = time_function(0.1, fn, 1, 2)
    assert name == fn.__qualname__
    assert value == 3

def test_time_with_lambda_with_name_specified():
    fn = lambda a, b: a + b

    _, name, _, _ = time_function(0.1, fn, 1, 2, method_name='add')
    assert name == 'add'
