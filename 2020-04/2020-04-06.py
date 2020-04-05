# 对2020-04-05.py文件中的解析数据进行封装

import csv
import os

def getDataFromCsv():
    user_test_data = []
    # 先获取项目的dir目录(如：D:/python_homework)
    dir_path = os.path.dirname(os.path.dirname(__file__))
    print("获取项目的路径：" + dir_path)

    # 然后根据项目的路径，找到data的目录
    csvfile = os.path.join(dir_path, 'data/user.csv')
    print("数据文件user.csv的路径：" + csvfile)

    # 打开数据源文件，并读取数据
    with open(csvfile, encoding='utf8') as file:
        filedata = csv.reader(file)

        # 去掉第一行
        next(filedata)
        for x in filedata:
            user_test_data.append(x)
        return user_test_data

data = getDataFromCsv()
print(data)