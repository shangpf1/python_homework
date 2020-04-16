"""
如果把登录操作放到前置操作里，那么就需要@pytest.fixture装饰器，传参就用默认的request参数
user=request.param 这一步就接收传入的参数，本案例是传入一个参数的情况
"""
import pytest


# 测试账号数据
test_user_data=["admin1","admin2"]
@pytest.fixture(scope="module")
def login(request):
    user=request.param
    print("登录用户：%s"%user)
    return user

@pytest.mark.parametrize("login",test_user_data,indirect=True)
def test_login(login):
    a = login
    print("测试用例中login的返回值：%s"%a)
    assert a != ""

if __name__=="__main__":
    pytest.main(["-s","test_login02.py"])