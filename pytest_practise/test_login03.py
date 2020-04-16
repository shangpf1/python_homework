"""
如果用到@pytest.fixture，里面用2个参数，可以把多个参数用一个字典存储，这样最终还是只传一个参数
不同的参数再从字典里取对应的key值就行，如：user=request.param["user"]
"""
import pytest

# 测试账户数据
test_user_data=[{"user":"admin","psw":"123456"},
                {"user":"admin","psw":""}]

@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("登录账户：%s"%user)
    print("登录密码：%s"%psw)
    if psw:
        return True
    else:
        return False
# 添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数
@pytest.mark.parametrize("login",test_user_data,indirect=True)
# 登录用例
def test_login(login):
    a = login
    print("测试用例中login的返回值：%s"%a)
    assert a,"失败原因：密码为空"

if __name__=="__main__":
    pytest.main(["-s","test_login03.py"])