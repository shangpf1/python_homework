# 微博爬虫实践2（将搜索的结果内容写入文件excel中）

from selenium import webdriver
import xlwt

driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&pvid=adc61cd71afd4c659067ee421d4308f2')


desc_eles = driver.find_elements_by_css_selector('div.p-name.p-name-type-2')
# 手机的价格
price_eles = driver.find_elements_by_css_selector('li.gl-item div.p-price')

# print(len(eles))

count = len(price_eles)
wd = xlwt.Workbook()
ws = wd.add_sheet('手机')

ws.write(0,0,'手机')
ws.write(0,1,'价格')

for index in range(count):
    ws.write(index+1,0,desc_eles[index].text)
    ws.write(index+1,1,price_eles[index].text)

wd.save('phone.xls')


# for index in range(len(eles)):
#     print(eles[index].text)