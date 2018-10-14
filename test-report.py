import unittest
import HTMLReport

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

def suite():
    suite = unittest.TestSuite()
    suite.addTest(CnodeTest('test_01register'))
    suite.addTest(CnodeTest('test_02login'))
    return suite
        

if __name__ == '__main__':
    suite=suite()


   # 测试用例执行器
    runner = HTMLReport.TestRunner(report_file_name='test',  # 报告文件名，默认“test”
                                output_path='report',  # 保存文件夹名，默认“report”
                                verbosity=2,  # 控制台输出详细程度，默认 2
                                title='测试报告',  # 报告标题，默认“测试报告”
                                description='无测试描述',  # 报告描述，默认“无测试描述”
                                thread_count=1,  # 并发线程数量（无序执行测试），默认数量 1
                                # 是否按照套件添加(addTests)顺序执行，
                                sequential_execution=True
                                # 会等待一个addTests执行完成，再执行下一个，默认 False
                                )
    # 执行测试用例套件
    runner.run(suite)

