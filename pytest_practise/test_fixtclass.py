# test_fixtclass.py
# coding:utf-8
import pytest
# 类和方法

class TestCse():

    def setup(self):
        print("setup:每个用例开始前执行")

    def teardown(self):
        print("teardown:每个用例结束后执行")


    def setup_class(self):
        print("setup_class:所有用例执行前")

    def teardown_class(self):
        print("teardown_class:所有用例执行后（完）")

    def setup_method(self):
        print("setup_method:每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:每个用例结束后执行")

    def test_1(self):
        print("正在执行----test_one")
        x = "this"
        assert 's' in x

    def test_2(self):
        print("正在执行----test_two")
        a = "hello"
        b = "hello world"
        assert a in b

# 备注：-s参数是为了显示用例的打印信息。 -q参数只显示结果，不显示过程
if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])

# 备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可
"""
运行结果：
setup_class:所有用例执行前
setup_method:每个用例开始前执行
setup:每个用例开始前执行
PASSED                                [ 50%]正在执行----test_one
teardown:每个用例结束后执行
teardown_method:每个用例结束后执行

setup_method:每个用例开始前执行
setup:每个用例开始前执行
PASSED                                [100%]正在执行----test_two
teardown:每个用例结束后执行
teardown_method:每个用例结束后执行
teardown_class:所有用例执行后（完）


============================== 2 passed in 0.02s ==============================

Process finished with exit code 0
"""