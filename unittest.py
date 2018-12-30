import unittest


# 定义一个加法的函数
def add(x,y):
    return x+y

# 定义一个减法函数
def minus(x,y):
    return x-y

# 定义一个乘法函数
def multi(x,y):
    return x*y

# 定义一个除法函数
def divide(x,y):
    return x/y

class TestFunc(unittest.TestCase):
    # 继承自unittest.TestCase
    # 重写TestCase的setUp()、tearDown()方法：在每个测试方法执行前以及执行后各执行一次
    def setUp(self):
        print("do something before test : prepare environment")

    def tearDown(self):
        print("do something after test : clean up ")
    
    # 测试方法均已test开头，否则是不被unittest识别的
    def test_add(self):
        print("add:")
        self.assertEqual(3,add(1,2))

    def test_minus(self):
        print("minus")
        self.assertEqual(3,minus(5,2))

    def test_multi(self):
        print("multi")
        self.assertEqual(6,multi(2 ,3))

    def test_divide(self):
        print("divide")
        self.assertEqual(2,divide(4,2))
        

if __name__ == '__main__':
# 在main()中加verbosity参数，可以控制输出的错误报告的详细程度
# verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)


# 执行结果：
test_add (__main__.TestFunc) ... do something before test : prepare environment
add:
do something after test : clean up
ok
test_divide (__main__.TestFunc) ... do something before test : prepare environment
divide
do something after test : clean up
ok
test_minus (__main__.TestFunc) ... do something before test : prepare environment
minus
do something after test : clean up
ok
test_multi (__main__.TestFunc) ... do something before test : prepare environment
multi
do something after test : clean up
ok

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK