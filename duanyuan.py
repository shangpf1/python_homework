import unittest

class CnodeTest(unittest.TestCase):

# 继承自unittest.TestCase
# 重写TestCase的setUp()、tearDown()方法：在每个测试方法执行前以及执行后各执行一次
# 访问数据库可以用此方法
    @classmethod
    def setUpClass(self):
        print('this is setupclass')

# 打开浏览器时用此方法
    def setUp(self):
        print('this is setup')

# 测试方法均已test开头，否则是不被unittest识别的
    def test_01register(self):
        print('****test_01register')

    def test_02login(self):
        print('****test_02login')

# 截屏可以用此方法
    def tearDown(self):
        print('this is teardown')

# 关闭浏览器可以用此方法
    @classmethod
    def tearDownClass(self):
        print('this is teardownclass')
        

if __name__ == '__main__':
# 在main()中加verbosity参数，可以控制输出的错误报告的详细程度
# verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)


# 执行结果：
this is setupclass
test_01register (__main__.CnodeTest) ... this is setup
****test_01register
this is teardown
ok
test_02login (__main__.CnodeTest) ... this is setup
****test_02login
this is teardown
ok
this is teardownclass

----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
