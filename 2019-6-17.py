
# map()   处理序列中的每个元素，得到的结果时一个‘列表’，该‘列表’元素个数及位置与原来一样（也就是说把所有的元素处理一遍）
# filter()  遍历序列中的每个元素，判断每个元素得到布尔值，如果是true则留下来

people = [
    {'name':'alex','age':100},
    {'name':'Ben','age':10000},
    {'name':'Joy','age':18},
    {'name':'Alen','age':8000},
]

print(list(filter(lambda p:p['age']<=18,people)))


# reduce()  处理一个序列，然后把序列合并操作 (也就是说将所有的数据压缩到一起)

from functools import reduce

print(reduce(lambda x,y:x+y,range(100)))    ## 结果：4950

print(reduce(lambda x,y:x+y,range(5),6))


print(reduce(lambda x,y:x+y,range(1,101)))