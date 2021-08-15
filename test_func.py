from main import func

def test_func_good1():
    c=func(10, 5)
    print(c)
    assert func(15, 5)==15