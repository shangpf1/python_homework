'''
unittest
运行结果：
setUpClass...
test_01register (__main__.CnodeTest) ... this is setup...
this is teardown...
ok
test_02login (__main__.CnodeTest) ... this is setup...
this is teardown...
FAIL
tearDownClass

======================================================================
FAIL: test_02login (__main__.CnodeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "2018-01-24.py", line 20, in test_02login
    self.assertEqual(1,2)
AssertionError: 1 != 2

----------------------------------------------------------------------
Ran 2 tests in 0.003s

FAILED (failures=1)

'''

import unittest

class CnodeTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        print('setUpClass...')

    def setUp(self):
        print('this is setup...')

    def test_01register(self):
        pass

    def test_02login(self):
        #pass
        self.assertEqual(1,2)

    def tearDown(self):
        print('this is teardown...')
    

    @classmethod
    def tearDownClass(self):
        print('tearDownClass')

    


if __name__ == '__main__':
    unittest.main(verbosity=2)

