import os
import csv

# get csv filepath   D:\python_homework\data\userinfo.csv
filepath = os.path.join(os.getcwd(),'data','userinfo.csv')
print(filepath)

# open filepath
f = open(filepath)

user = []
# reader file
reader = csv.reader(f)
print(reader)  #打印结果：<_csv.reader object at 0x000001773A1FEE80>

next(reader,None)

# 需要加上此循环进行遍历，不然会打印出内存地址
for row in reader:
    # print(row)
    user.append(row)
print(user)


"""
打印结果中有第一行，需要去掉，故需要进行迭代 next(reader,None)
['username', 'password', 're_password', 'email']
['lifei123', '123456', '123456', '208418427@163.com']
['hj@%"?#$', '123456', '123456', '208418427@163.com']
['lifei123', '      ', '123456', '208418427@163.com']
['lifei123', '123456', '686888', '208418427@163.com']
['lifei123', '123456', '123456', ' <?tdh-=']

"""