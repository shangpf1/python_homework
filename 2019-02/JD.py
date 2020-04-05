# 查找多个元素（京东官网手机价格）

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=9434cb2daf7c4351a929631cf56f52c3')

driver.maximize_window()

# 手机的价格
eles = driver.find_elements_by_css_selector('li[class="gl-item"] div.p-price')
print(len(eles))

# 打印出所有手机的价格
for index in range(len(eles)):
    print(eles[index].text)

