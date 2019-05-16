# 打印当前时间  格式：xxx年xxx月xxx日 xxx时xxx分xxx秒
import time
ticks = time.localtime(time.time())
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S',ticks))
# 运行结果：2019-05-16 13:53:28 当前系统的时间哈~




# append()和extend()的区别
"""
append() 方法用于在列表末尾添加新的对象。 
extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表

"""

# append() 在list后面添加相应字符,如果后面添加的是一个列表也会当一个整体的
list = ['a','b','c']
list.append(5)
print(list)
# 结果：['a', 'b', 'c', 5]



# extend() 将添加的列表中的内容打散拼接起来的，可以在下面用append()看下效果
s1 = [2,6]
s2 = ['y','k','t']
s1.extend(s2)
print(s1)
# 运行结果：[2, 6, 'y', 'k', 't']



# 实践：打印1~100所有的偶数
h = []
for i in range(1,101):
    if i%2==0:
        h.append(i)
print(h)
# 运行结果：[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86,
# 88, 90, 92, 94, 96, 98, 100]