
# 自定义函数--求和
# 方法一：
def sum(a,b):
    return a+b
y = sum(1,3)
print(y)

# 方法二：
y1 = lambda a1,b1:a1+b1
print(y1(1,5))


# 列表中函数的平方
# 方法一：
list = [1,3,4,5,6]
res=[]
for i in list:
    res.append(i**2)
print(res)

# 方法二：
# 定义一个方法，直接调用此函数
def map_test(array):
    res1 = []
    for i1 in array:
        res1.append(i1**2)
    return res1
res1 = map_test(list)
print(res1)
print('-----------------分 -- 割 -- 法------------------')
print('************以下为封装后，直接进行调用************')

num = [2,3,4]
# 自增函数
def add_one(x):
    return x+1

# 自减函数
def reduce_one(y):
    return y-1


# 把上面2个函数的的逻辑封装到此函数中
def map_test1(func,array):
    res1 = []
    for i2 in array:
        yt = func(i2)   # add_one(i2)
        res1.append(yt)
    return res1

# print(map_test1(add_one,num))
print(map_test1(lambda x:x+1,num))

# print(map_test1(reduce_one,num))
print(map_test1(lambda x:x-1,num))

# 平方
print(map_test1(lambda x:x**2,num))


"""
运行结果如下：

4
6
[1, 9, 16, 25, 36]
[1, 9, 16, 25, 36]
-----------------分 -- 割 -- 法------------------
************以下为封装后，直接进行调用************
[3, 4, 5]
[1, 2, 3]
[4, 9, 16]

"""