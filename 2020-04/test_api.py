# 后面的2个接口需要用第一个接口里返回数据作为其传入参数
import requests
import json

s = requests.session()
print(s.headers)
print(s.cookies)

# 1、登录接口
url = "http://49.235.92.12:9000/api/v1/login"
body = {
         "username":"test",
         "password":"123456"
}

# 转json
r = requests.post(url,json=body)
token = r.json().get("token")
print("取到的token: %s"%token)

h = {
      "Authorization": "Token  %s"%token
}

s.headers.update(h)     #更新到session会话
# 更新后的头部
print(s.headers)


# 2、登录后获取用户信息接口
url2 = "http://49.235.92.12:9000/api/v1/userinfo"
r2 = s.get(url2)
print(r2.text)

# 取 mail
print(r2.json()['data'])
print(r2.json()['data'][0])
print(r2.json()['data'][0]['mail'])

# 3、修改个人信息
url3 = "http://49.235.92.12:9000/api/v1/userinfo"
body3 ={
    "name": "test",
    "sex": "M",
    "age": 20,
    "mail": "283340479@qq.com"
    }
r3 = s.post(url3,json=body3)
print(r3.text)
''''
1、登录接口
{'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
<RequestsCookieJar[]>
取到的token: 6c6e8ee2ecb1e51498e8d50938d060bfd87e4e69
{'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Token  6c6e8ee2ecb1e51498e8d50938d060bfd87e4e69'}

2、登录后获取用户信息接口
{"msg":"sucess!","code":0,"data":[{"id":105,"name":"test","sex":"M","age":20,"mail":"283340479@qq.com","create_time":"2020-04-22"}]}
[{'id': 105, 'name': 'test', 'sex': 'M', 'age': 20, 'mail': '283340479@qq.com', 'create_time': '2020-04-22'}]
{'id': 105, 'name': 'test', 'sex': 'M', 'age': 20, 'mail': '283340479@qq.com', 'create_time': '2020-04-22'}
283340479@qq.com

3、修改个人信息
{"message":"update some data!","code":0,"data":{"name":"test","sex":"M","age":20,"mail":"283340479@qq.com"}}
'''