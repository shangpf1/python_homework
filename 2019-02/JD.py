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

# 运行结果：
"""
30
￥2999.00
￥1299.00
￥1299.00
￥5899.00
￥3298.00
￥2799.00
￥799.00
￥3598.00
￥3299.00
￥1199.00
￥899.00
￥3499.00
￥799.00
￥1599.00
￥3999.00
￥799.00
￥2989.00
￥6199.00
￥9699.00
￥1598.00
￥3299.00
￥3799.00
￥2198.00
￥4699.00
￥5499.00
￥1499.00
￥2298.00
￥1099.00
￥1999.00
￥1898.00
"""

