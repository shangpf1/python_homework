
# 列表中函数的平方
# 方法一：
list = [1,3,4,5,6]
res=[]
for i in list:
    res.append(i**2)
print(res)

# 方法二：
# 定义一个方法，直接调用此函数

num = [4,5,6]
def map_test(array):
    res = []
    for i in array:
        res.append(i**2)
    return res
print(map_test(num))

print('-----------------分 -- 割 -- 法------------------')

# 自增函数
def add_one(x):
    return x+1

# 对函数进行封装
def map_test1(func,array):
    res = []
    for i in array:
        yt = func(i)
        res.append(yt)
    return res
# print(map_test1(add_one,num))
print(map_test1(lambda x:x+1,num))

