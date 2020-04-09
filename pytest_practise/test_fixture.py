import pytest

"""
1.firture相对于setup和teardown来说应该有以下几点优势:

1)命名方式灵活，不局限于setup和teardown这几个命名
2)conftest.py 配置里可以实现数据共享，不需要import就能自动找到一些配置
3)scope=”module” 可以实现多个.py跨文件共享前置
4)scope=”session” 以实现多个.py跨文件使用一个session来完成多个用例
"""

# 如果@pytest.fixture()里面没有参数，那么默认scope=”function”，也就是此时的级别的function，针对函数有效
@pytest.fixture()
def login():
    print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后，其动作1")

"""
不需要login
"""
def test_s2():
    print("用例2：不需要登录，操作2")

def test_s3(login):
    print("用例3：登录之后操作3")

if __name__ == "__main__":
    pytest.main("s","test_fixture.py")



