import pytest
"""
pytest.mark.parametrize装饰器可以实现测试用例参数化。
1、这里是一个实现检查一定的输入和期望输出测试功能的典型例子
2、它也可以标记单个测试实例在参数化，例如使用内置的mark.xfail
   标记为失败的用例就不运行了，直接跳过显示xfailed
"""
# @pytest.mark.parametrize("test_input,expected",
#                          [("3+5",8),
#                           ("2+4",6),
#                           ("6 * 9",54),
#                           ])

@pytest.mark.parametrize("test_input,expected",
                         [("3+5",8),
                          ("2+4",6),
                          pytest.param("6 * 9",42,marks=pytest.mark.xfail),

                          ])
def test_eval(test_input,expected):
    assert eval(test_input)==expected

if __name__=="__main__":
    pytest(["s","test_canshu1.py"])
