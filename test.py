'''
运行结果：
0 ===> ['xiaoming', '123456', '123456', 'xm@1234.com']
0 : 0 ===> xiaoming
0 : 1 ===> 123456
0 : 2 ===> 123456
0 : 3 ===> xm@1234.com
1 ===> ['', '123456', '123456', 'xm@1234.com']
1 : 0 ===>
1 : 1 ===> 123456
1 : 2 ===> 123456
1 : 3 ===> xm@1234.com
2 ===> ['xiaoming', '', '123456', 'xm@1234.com']
2 : 0 ===> xiaoming
2 : 1 ===>
2 : 2 ===> 123456
2 : 3 ===> xm@1234.com
3 ===> ['xiaoming', '123456', '', 'xm@1234.com']
3 : 0 ===> xiaoming
3 : 1 ===> 123456
3 : 2 ===>
3 : 3 ===> xm@1234.com

'''

from selenium import webdriver


test_data=[
    ['xiaoming','123456','123456','xm@1234.com'],
    ['','123456','123456','xm@1234.com'],
    ['xiaoming','','123456','xm@1234.com'],
    ['xiaoming','123456','','xm@1234.com']
]

for x in range(len(test_data)):
    print(x,"===>",test_data[x])
    for y in range(len(test_data[x])):
        print(x,":",y,"===>",test_data[x][y])
   


