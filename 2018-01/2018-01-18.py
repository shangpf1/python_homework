# 读取 csv文件中的相关信息(CNode论坛注册信息)

import os 
import csv

filepath = os.path.join(os.getcwd(),'data','userinfo.csv')

#print(filepath)

# 打开csv文件
f = open(filepath)
read = csv.reader(f)
print(read)


# 打印出 csv文件中测试用例信息
for row in read:
    print(row)

