import json

a = '{"username":"xiaoming","age":12}'

a1 = json.loads(a)
print(type(a1),a1)

b = eval(a)
print(type(b),b)



# 下列清空 json.loads 将会报错, eval 仍然可以解析
a = "{'username':'xiaoming','age':12}"

# a1 = json.loads(a)   #loads 解析失败
# print(type(a1),a1)

b = eval(a)
print(type(b),b)

print(eval('1+1'))


import base64
import json
"""
dict==>bytes 字典如何转换为字节类型的数据
1. dict == > str
json.dumps()
"""
testdata = {
    "accesstoken":"{{token}}",
    "title":"baiwriter",
    "tab":"ask",
    "content":"woshishuiyeahyeah"
}

# dict 转 str
testdata_str = json.dumps(testdata)
print(testdata_str,type(testdata_str))
# str 转 bytes   encode()方法
testdata_bytes = testdata_str.encode()
print(testdata_bytes,type(testdata_bytes))
# base64 encode
b64_encode = base64.b64encode(testdata_bytes)
print(b64_encode)

# base64 解密
b64_decode = base64.b64decode(b64_encode)
print(b64_decode)