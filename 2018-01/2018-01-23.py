
'''
unittest
运行结果：
test_01register (__main__.CnodeTest) ... ok
test_02login (__main__.CnodeTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

'''

import unittest

class CnodeTest(unittest.TestCase):
    def test_01register(self):
        pass

    def test_02login(self):
        pass
      

if __name__ == '__main__':
    unittest.main(verbosity=2)
