import pytest
"""
当用例a失败的时候，如果用例b和用例c都是依赖于第一个用例的结果，那可以直接跳过用例b和c的测试，直接给他标记失败xfail
用到的场景，登录是第一个用例，登录之后的操作b是第二个用例，登录之后操作c是第三个用例，很明显三个用例都会走到登录。
如果登录都失败了，那后面2个用例就没测试必要了，直接跳过，并且标记为失败用例，这样可以节省用例时间。
"""
canshu=[{"user":"admin","psw":""}]
@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("正在操作登录，账号%s,密码%s"%(user,psw))
    if psw:
        return True
    else:
        return False

@pytest.mark.parametrize("login",canshu,indirect=True)
class Test_xx():
    def test_01(self,login):
        result = login
        print("用例1：%s"%result)
        assert result == True

    def test_02(self,login):
        result = login
        print("用例2：%s"%result)
        if not result:
            pytest.xfail("登录不成功，标记为xfail")
        assert 1 == 1

    def test_03(self,login):
        result = login
        print("用例3：%s"%result)
        if not result:
            pytest.xfail("登录不成功，标记为xfail")
        assert 1 == 1


if __name__=="__main__":
    pytest.main(["-s","test_xfail.py"])

# 运行结果：用例1失败，用例2、用例3都是xfail