from selenium import webdriver
import time

driver = webdriver.Chrome()

time.sleep(5)
driver.get("http://118.31.19.120:3000/signin")

# driver.find_element_by_id("name").send_keys("testuser20")
driver.find_element_by_css_selector("#name").send_keys("testuser15")
# driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456")
driver.find_element_by_class_name("span-primary").click()

# 退出
driver.quit()