# test_fixt.py
# coding:utf-8
import pytest
# 函数式

def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module:整个.py模块只执行一次")
    print("比如：所有用例结束后只关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束后都会执行")

def test_1():
    print("正在执行----test_one")
    x = "this"
    assert 's' in x

def test_2():
    print("正在执行----test_two")
    a = "hello"
    b = "hello world"
    assert a in b

# 备注：-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
if __name__ == "__main__":
    pytest.main(["-q", "test_fixt.py"])


"""
运行结果：

test_fixt.py::test_1 setup_module：整个.py模块只执行一次
比如：所有用例开始前只打开一次浏览器
setup_function：每个用例开始前都会执行
PASSED                                              [ 50%]正在执行----test_one
teardown_function：每个用例结束后都会执行

test_fixt.py::test_2 setup_function：每个用例开始前都会执行
PASSED                                              [100%]正在执行----test_two
teardown_function：每个用例结束后都会执行
teardown_module:整个.py模块只执行一次
比如：所有用例结束后只关闭浏览器


============================== 2 passed in 0.03s ==============================

Process finished with exit code 0

"""