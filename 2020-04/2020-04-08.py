'''
使用fixture
通过@pytest.fixture 传递参数
@pytest.fixture
scope： 作用域
autouse： 是否自动加载
name ： 引用名称
parmas： 参数
ids：执行显示函数名称后缀
'''

import pytest
import requests

base_url = "http://39.107.96.138:3000/api/v1/"
testdata = {
        "accesstoken":"49b2e830-4305-475d-b6b5-52287cc5daaa",
        "title":"2313131231231232",
        "tab":"ask",
        "content":"xxxxxxxxxxxxx"
    }

@pytest.fixture(scope="module",autouse=True,name="topic_id")
def newtopic():
    url = base_url + 'topics'
    r = requests.post(url, json=testdata)
    jsonData = r.json()

    return jsonData['topic_id']


def test_update_topic(topic_id):
    """
    编辑话题
    :return:
    """
    print("test_update_topic",topic_id)

def test_collect_topic(topic_id):
    """
    收藏话题
    :return:
    """
    print("test_collect_topic",topic_id)


def test_reply_topic(topic_id):
    """
    回复话题
    :return:
    """
    print("test_reply_topic",topic_id)