import unittest

class CnodeTest(unittest.TestCase):

# 访问数据库可以用此方法
    @classmethod
    def setUpClass(self):
        print('this is setupclass')

# 打开浏览器时用此方法
    def setUp(self):
        print('this is setup')

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
    unittest.main(verbosity=2)
