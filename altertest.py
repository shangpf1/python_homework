
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time


driver = webdriver.Chrome()
# 打开登录页面
driver.get("file:///D:/Learn-python/python_homework/alert.html")

driver.find_element_by_tag_name('button').click()
time.sleep(3)
Alert(driver).accept()