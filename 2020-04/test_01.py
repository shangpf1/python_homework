import random
print(random.random())

ph = ['13','15','17','17','18']
num=['1','2','3','4','5','6','7','8','9','0']
phnum = ''

for x in range(9):
    phnum+=random.choice(num)
phnum=random.choice(ph)+phnum
print(phnum)


sum = 0
for x in range(0,101):
    if x % 2 == 0:
        sum += x
print(sum)


num = []
for y in range(0,101):
    if y % 2 != 0:
        num.append(y)
print(num)


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return n*func(n-1)
print(func(5))


a = 0
b = 1
while b < 100:
    print(b ,end=' ')
    a , b = b , a + b

# 字符串切割
# 已知的一个字符串"hello_world_haha"，需要的结果是 ['hello', 'world', 'haha']
a = "hello_world_haha"
b = a.split("_")
print(end='\n')
print(b)


for x in range(1,10):
    for y in range(1,x+1):
        print('{}*{}={}\t'.format(x,y,x*y),end='')
    print()