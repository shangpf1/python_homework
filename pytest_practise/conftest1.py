# conftest1.py
import pytest
# 命令中 加上  —self-contained-html 失败重跑

@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度页面")
    yield
    print("执行teardown")
    print("最后关闭浏览器")

def test_s1(open):
    print("用例1：搜索python-1")

    # 如果此用例异常，则不会影响其他用例
    raise NameError    #模拟异常


def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__=="__main__":
    pytest.main("s","test_f2.py")


 # pytest conftest1.py --html=./report/report2.html --self-contained-html


