"""
为提高代码复用性，会写个函数，然后不同的用例去调用这个函数（比如：登录）

## 把登录单独成立，写一个函数，传2个参数user和psw，写用例的时候调用登录函数，输入几组user,psw参数化登录用例
测试用例传参需要用装饰器@pytest.mark.parametrize，里面写两个参数

第一个参数是字符串，多个参数中间用逗号隔开
第二个参数是list,多组数据用元祖类型

今天运行pytest文件时报没运行case, 原因时现在的python3放弃pytest-allure-adaptor库了，需要将其卸载即可
 卸载命令： pip uninstall pytest-allure-adaptor

"""
import pytest

# 测试登录数据
test_login_data = [("admin", "111111"),  ("admin", "")]

def login(user, psw):
    '''普通登录函数'''
    print("登录账户：%s"%user)
    print("登录密码：%s"%psw)
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("user, psw", test_login_data)
def test_login(user, psw):
    '''登录用例'''
    result = login(user, psw)
    assert result == True, "失败原因：密码为空"


# if __name__=="__main__":
#     pytest.main(["-s","test_login01.py"])

if __name__ == "__main__":
    pytest.main(["-s", "test_login01.py"])