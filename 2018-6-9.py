from selenium import webdriver
import time

# 滑块的模仿  需要调用此库 ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()


# 阿里云
driver.get("https://account.aliyun.com/register/register.htm")

# driver.find_element_by_css_selector("#nick").send_keys("123456")
# driver.find_element_by_xpath('//*[@id="rePassword"]').send_keys("123456")
# driver.find_element_by_css_selector("#mobile").send_keys("15029946654")


# 向右滑动的滑块 ActionChains
driver.switch_to_frame('alibaba-register-box')
ele = driver.find_element_by_id('nc_1_n1z')

ActionChains(driver).drag_and_drop_by_offset(ele,200,200).pause(1).drag_and_drop_by_offset(ele,200,200).perform()

# driver.find_element_by_class_name("next-btn next-btn-primary next-btn-large").click()