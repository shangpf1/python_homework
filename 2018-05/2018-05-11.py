from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

# 定位元素
eles = driver.find_elements_by_class_name("mnav")


print("info:",len(eles),driver.current_url)

urls = []

for ele in eles:
    herf = ele.get_attribute("href")
    name = ele.get_attribute("name")
    print("text:",ele.text,"href：",herf,"name:",name)
    urls.append(herf)



# 结果如下示：

# info: 6 https://www.baidu.com/
# text: 新闻 href： http://news.baidu.com/ name: tj_trnews
# text: hao123 href： https://www.hao123.com/ name: tj_trhao123
# text: 地图 href： http://map.baidu.com/ name: tj_trmap
# text: 视频 href： http://v.baidu.com/ name: tj_trvideo
# text: 贴吧 href： http://tieba.baidu.com/ name: tj_trtieba
# text: 学术 href： http://xueshu.baidu.com/ name: tj_trxueshu