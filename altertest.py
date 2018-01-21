'''
跳出删除提示框

'''
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()
# 打开登录页面
driver.get("file:///D:/Learn-python/python_homework/alert.html")

# 点击按钮
driver.find_element_by_tag_name('button').click()

# 延时
time.sleep(3)

# 自动关闭提示框
Alert(driver).accept()