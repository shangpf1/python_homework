import pytest
import pytest_html
# pytest-HTML是一个插件，pytest用于生成测试结果的HTML报告。兼容Python 2.7,3.6。
# pip install pytest-html
# 执行方法： pytest —html=report.html

"""
导入pytest_html库，运行下面的命令可以生成测试报告

pytest test_report.py --html=./report/report1.html
"""
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度页面")

def test_s1(open):
    print("用例1：搜索python-1")


def test_s2(open):
    print("用例2：搜索python-2")

def test_s3(open):
    print("用例3：搜索python-3")

if __name__=="__main__":
    pytest.main("s","test_f2.py")


"""
控制台执行命令： pytest test_report.py --html=./report/report1.html
============================================================ test session starts ============================================================
platform win32 -- Python 3.6.3, pytest-5.4.1, py-1.7.0, pluggy-0.13.1
rootdir: D:\python_homework\pytest_practise
plugins: html-2.1.1, metadata-1.8.0
collected 3 items                                                                                                                            

test_report.py ...                                                                                                                     [100%]

---------------------------- generated html file: file://D:\python_homework\pytest_practise\report\report1.html -----------------------------
============================================================= 3 passed in 0.05s =============================================================
"""