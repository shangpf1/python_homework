# 登录函数，获取token
import requests

def login(s):
    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
         "username":"test",
         "password":"123456"
    }

    r = s.post(url,data=body)
    print(r.json())

    # 获取token
    token = r.json().get("token")
    print("取到的token: %s" % token)

    h = {
        "Authorization":"token %s" %token
    }

    s.headers.update(h)   # 更新到 session会话
    return token

if __name__ == '__main__':
    s = requests.session()  #会话   代码里的浏览器，模拟浏览器的功能
    login(s)
    print(s.headers)