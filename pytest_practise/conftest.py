# coding:utf-8
import pytest

"""
上面一个案例是在同一个.py文件中，多个用例调用一个登陆功能，如果有多个.py的文件都需要调用这个登陆功能的话，那就不能把登陆写到用例里面去了。
此时应该要有一个配置文件，单独管理一些预置的操作场景，pytest里面默认读取conftest.py里面的配置

conftest.py配置需要注意以下点：

1)conftest.py配置脚本名称是固定的，不能改名称
2)conftest.py与运行的用例要在同一个pakage下，并且有init.py文件
3)不需要import导入 conftest.py，pytest用例会自动查找
"""
@pytest.fixture()
def login():
    print("输入账号，密码先登录")