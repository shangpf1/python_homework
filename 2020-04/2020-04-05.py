# 此文件执行需要data中的user.csv数据源（用户数据源）
import os
import csv

# 获取当前文件的路径（如：D:\python_homework\2020-04）
dir=os.path.dirname(__file__)
print("获取当前文件路径:" +dir)

# 先获取项目的dir目录(如：D:/python_homework)
dir_path=os.path.dirname(os.path.dirname(__file__))
print("获取项目的路径："+dir_path)

# 然后根据项目的路径，找到data的目录
csvfile=os.path.join(dir_path,'data/user.csv')
print("数据文件user.csv的路径："+csvfile)

# 打印出数据里的数据
with open(csvfile,encoding='utf8') as file:
    filedata=csv.reader(file)
    next(filedata)
    for x in filedata:
        print(x)

# 对数据里的数据进行处理
csvdata=[]
with open(csvfile,encoding='utf8') as file:
    filedata=csv.reader(file)
    next(filedata)
    for x in filedata:
        # print(x)
        csvdata.append(x)

print('------------------------------------------------------------------------------')
print("对数据里的数据进行处理,如下：")
print(csvdata)

'''

获取当前文件路径:D:/python_homework/2020-04
获取项目的路径：D:/python_homework
数据文件user.csv的路径：D:/python_homework\data/user.csv
['1', '男', '23', '尚鹏飞', '陕西咸阳']
['2', '女', '60', '李飞', '河南洛阳']
['3', '男', '54', '王晓', '上海市']
['4', '女', '23', '张淼', '安徽安庆']
['5', '女', '12', '赵倩', '江苏南京']
-----------------------------------------------------------------------
对数据里的数据进行处理,如下：
[['1', '男', '23', '尚鹏飞', '陕西咸阳'], ['2', '女', '60', '李飞', '河南洛阳'], ['3', '男', '54', '王晓', '上海市'], ['4', '女', '23', '张淼', '安徽安庆'], ['5', '女', '12', '赵倩', '江苏南京']]

'''