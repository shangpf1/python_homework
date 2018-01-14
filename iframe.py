from selenium import webdriver
import time

# 安居客

driver = webdriver.Chrome()
# 打开登录页面
driver.get("https://login.anjuke.com/login/form")

# 因为iframe 的关系
# switch_to iframe http://selenium-python.readthedocs.io/api.html?highlight=iframe
#  使用 iframe 的id 找到iframe
driver.switch_to_frame("iframeLoginIfm")
# 输入用户名
driver.find_element_by_id('phoneIpt').send_keys('18791042625')


# 输入密码