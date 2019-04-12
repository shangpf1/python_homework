"""
处理excel 文件，文件不能用xlrd命名，先要用一个文件data.xls并且有数据,我这里的数据是20行3列的数据

文档地址 https://github.com/python-excel/xlrd
"""
# excel文件数据的读取，必须先安装此库 pip install xlrd
import xlrd

book = xlrd.open_workbook('data.xls')
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))

# 这里的colx不能是3，否则会越界，因为只有3列数据
print("Cell D30 is {0}".format(sh.cell_value(rowx=20, colx=2)))
for rx in range(sh.nrows):
    print(sh.row(rx))


# 运行结果如下：
"""
The number of worksheets is 1
Worksheet name(s): ['Sheet']
Sheet 21 3
Cell D30 is 92.0
[text:'学号', text:'姓名', text:'成绩']
[text:'c0001', text:'lucy', number:80.0]
[text:'c0002', text:'jame', number:90.0]
[text:'c0003', text:'jack', number:70.0]
[text:'c0004', text:'tom', number:96.0]
[text:'c0005', text:'lily', number:98.0]
[text:'c0006', text:'jim', number:99.0]
[text:'c0007', text:'thoma', number:100.0]
[text:'c0008', text:'王菲', number:90.0]
[text:'c0009', text:'李飞', number:98.0]
[text:'c0010', text:'张三', number:97.0]
[text:'c0011', text:'赵云', number:93.0]
[text:'c0012', text:'尚朋飞', number:86.0]
[text:'c0013', text:'李小璐', number:89.0]
[text:'c0014', text:'范斌', number:87.0]
[text:'c0015', text:'李冰冰', number:98.0]
[text:'c0016', text:'古天乐', number:99.0]
[text:'c0017', text:'于荣光', number:90.0]
[text:'c0018', text:'张柏芝', number:98.0]
[text:'c0019', text:'林志玲', number:93.0]
[text:'c0020', text:'green', number:92.0]
"""