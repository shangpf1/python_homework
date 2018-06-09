from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

# 此库主要是模拟鼠标 key_down（点击）  key_up（松开） 
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("http://118.31.19.120:3000/signin")

# 输入用户名和密码及登录
driver.find_element_by_id('name').send_keys("testuser3")
driver.find_element_by_id("pass").send_keys('123456')
driver.find_element_by_id("pass").submit()

# 点击发布话题
driver.find_element_by_css_selector('.span-success').click()

# 定位选择板块选项
driver.find_element_by_id('tab-value').click()

# 选择第3项 问答
driver.find_element_by_css_selector('#tab-value > option:nth-child(3)').click()

# 主题
driver.find_element_by_id('title').send_keys('helloworld')

# 文本内容部分
input_content = driver.find_element_by_css_selector('.CodeMirror-code')  # 定义光标定位的变量
input_content.click()          # 鼠标点击
ActionChains(driver).move_to_element(input_content).click().key_down(Keys.COMMAND).send_keys("btertrtrtytry").key_up(Keys.COMMAND).perform()

# ActionChains(driver).move_to_element(input_content).click().send_keys("hellowlrodl").perform()


# ActionChains(driver).click(input_content).send_keys_to_element(input_content,"dsdsdsdsdsdsdsds").perform()