# coding:utf-8
import pytest
# 单独运行test_fix1.py和test_fix2.py都能调用到login()方法，这样就能实现一些公共的操作可以单独拿出来了
# 此文件只要放到此包下任何地方都可以

def test_s1(login):
    print("用例1：登录之后其它动作111")

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fix1.py"])