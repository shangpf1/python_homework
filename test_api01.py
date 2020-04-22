import requests
import re     # 需要用到正则表达式  其为库

s = requests.session()
print(s.cookies)

url = "http://49.235.92.12:9000/admin/"
r1 = s.get(url)
print(s.cookies)

# 获取页面的 csrfmiddlewaretoken
# print(r1.text)      #获取页面源码

# 知道前后取中间，遇到字符串的加转义字符     -----正则表达式  需要引入库 import re
# name='csrfmiddlewaretoken' value='(.+?)'

csrfmiddlewaretoken = re.findall("name=\'csrfmiddlewaretoken\' value='(.+?)\'",r1.text)    # r1.text 为提取对象
print(csrfmiddlewaretoken)

print(csrfmiddlewaretoken[0])

# 登录
body = {
    "csrfmiddlewaretoken":csrfmiddlewaretoken[0],
    "username":"admin",
    "password":"yoyo123456",
    "next":"/admin/"
}

r = s.post(url,data=body)
# print(r.text)

if "Site administration | Django site admin" in r.text:
    print("登录成功")
else:
    print("登录失败")

# assert "欢迎您" in r.text
