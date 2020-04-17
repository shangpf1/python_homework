import pytest
"""
pytest可以支持自定义标记，自定义标记可以把一个web项目划分多个模块，然后指定模块名称执行。app自动化的时候，如果想android和ios公用一套代码时，
也可以使用标记功能，标明哪些是ios用例，哪些是android的，运行代码时候指定mark名称运行就可以
"""
# 以下用例，标记test_send_http()为webtest
@pytest.mark.webtest
def test_send_http():
    pass
def test_something_quick():
    pass
def test_another():
    pass

class TestClass:
    def test_method(self):
        pass

# 只运行用webtest标记的测试，cmd运行的时候，加个-m 参数，指定参数值webtest
# if __name__=="__main__":
#     pytest.main(["-s","test_server.py","-m=webtest"])

"""
# 如果不想执行标记webtest的用例，那就用”not webtest”
if __name__=="__main__":
    pytest.main(["-s","test_server.py","-m='not webtest'"])
"""


# 当然也能选择运行整个class
if __name__ == "__main__":
    pytest.main(["-v", "test_server.py::TestClass"])