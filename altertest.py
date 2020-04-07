'''
跳出删除提示框

'''
import os
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

# 先查找到alert.html 的路径
# dirname=os.path.dirname(os.path.dirname(__file__))
# file=os.path.join(dirname,'alert.html')
# print(file)

driver = webdriver.Chrome()
driver.maximize_window()

# 打开登录页面
driver.get("file:///D:/python_homework/alert.html")

# 点击按钮
driver.find_element_by_tag_name('button').click()

# 延时
time.sleep(1)

# 自动关闭提示框
Alert(driver).accept()
