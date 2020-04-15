import pytest
"""
pytest里面断言实际上就是python里面的assert断言方法，常用的有以下几种:

assert  xx  判断xx为真
assert not xx 判断xx不为真
assert a in b  判断b包含a
assert a == b 判断a等于b
assert a != b  判断a不等于b
"""
def is_true(a):
    if a > 0:
        return True
    else:
        return False

def test_01():
    # 断言 XX为真
    a = 5
    b = -1
    assert is_true(a)
    assert not is_true(b)    #一个用例中可以支持多个断言

def test_02():
    # 断言b包含a
    a = "hello"
    b = "hello world"
    assert a in b

def test_03():
    # 判断a等于b
    a = "haha"
    b ="haha"
    assert a == b

def test_04():
    # 判断a不等于b
    a = 3
    b =4
    assert a != b

if __name__=="__main__":
    pytest.main("s","test_assert.py")