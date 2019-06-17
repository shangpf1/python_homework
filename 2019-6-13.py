"""
我的练习作业03- python 高级排序-字符长度相同进行排序
"""

# 正序（关于正序排序，首先会按字符的长度排序，如果一样的话，会按字符正序的首字母的ASCII码大小排序）

strs = ['study','happy','thing']
print('s==>',ord('s'),'h===>',ord('h'),'t===>',ord('t'))
strs.sort()
print("正序排序为：",strs)  



"""
 倒序（关于倒序排序，和上面的正序刚好相反，从字符的末尾的字符大小进行排序，如果末尾字符相同，
 会按倒数第二位的字符大小排序，如此类推）
"""

print('g====',ord('g'),'y======',ord('y'),'p===',ord('p'),'d====',ord('d'))
strs.sort(key=len,reverse=True)
print("倒序排序为：",strs)