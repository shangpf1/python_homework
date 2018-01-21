# 解析 userinfo.csv文件

import csv


def  getDataFromCsv():
    all_test_data = []
    with open('./userinfo.csv') as filedata:
        # print(filedata)
        filereader = csv.reader(filedata)
        # print(filereader)

        next(filereader)  #去掉第一行数据：['username', 'password', 're_password', 'email']
        for row in filereader:
            # print(row)
            all_test_data.append(row)

        return all_test_data

data = getDataFromCsv()
print(data)    

