import requests

# 发布话题
base_url = "http://39.107.96.138:3000/api/v1/"
testdata = {
        "accesstoken":"49b2e830-4305-475d-b6b5-52287cc5daaa",
        "title":"231313123123126868686",
        "tab":"ask",
        "content":"嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿"
    }

def test_new_topic():
    url=base_url+'topics'
    r=requests.post(url,json=testdata)
    resData=r.json()

    assert r.status_code==200
    assert resData['success']
    print('test_new_topic,topicid:',resData['topic_id'])

    assert resData['topic_id'] is not None
    return resData['topic_id']
