# 爬虫（京东官网手机的名称及价格信息）并保存到excel中
# https://github.com/python-excel/xlwt  参考文档

import xlwt
from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=9434cb2daf7c4351a929631cf56f52c3')

driver.maximize_window()

# 手机的价格及描述
price_eles = driver.find_elements_by_css_selector('li[class="gl-item"] div.p-price')
desc_eles = driver.find_elements_by_css_selector('div.p-name.p-name-type-2')

count = len(price_eles)

# 创建一个表格，及sheet命名为'手机'
wd = xlwt.Workbook()
ws = wd.add_sheet('手机')

# 表格中第一行的各个字段描述
ws.write(0,0,'手机描述')
ws.write(0,1,'价格')

for index in range(count):
    ws.write(index+1,0,desc_eles[index].text)
    ws.write(index+1,1,price_eles[index].text)

wd.save('phone.xls')




