from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")


# 登录
# driver.find_element_by_css_selector("#u1 > a.lb").click()

# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

# 用户名密码登录
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys("15029946654")
# driver.find_element_by_css_selector("#TANGRAM__PSP_10__password").send_keys("123456")
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()


# 新闻
# driver.find_element_by_link_text("新闻").click()

# driver.find_element_by_partial_link_text("新").click()

# 地图
driver.find_element_by_css_selector('#u1 > a:nth-child(3)').click()   



