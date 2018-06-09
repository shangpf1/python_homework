from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("http://118.31.19.120:3000/signin")

#用户登录
driver.find_element_by_css_selector("#name").send_keys("testuser5")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456")
driver.find_element_by_class_name("span-primary").click()

#发布话题
driver.find_element_by_class_name("span-success").click()

#选择板块及定位选项（此处为第2项：分享）
driver.find_element_by_xpath('//*[@id="tab-value"]').click()
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()

# 主题
driver.find_element_by_css_selector("#title").send_keys("helloworld123")

#光标定位(Action Chains )
# http://selenium-python.readthedocs.io/api.html?highlight=att#module-selenium.webdriver.common.action_chains

# drag_and_drop 拖拽  不是太完美，有的不能拖拽的

# 光标元素定位并输入内容
menu=driver.find_element_by_class_name('CodeMirror-scroll')
ActionChains(driver).move_to_element(menu).click().perform()

#此部先不要定位，等运行后会鼠标点击文本位置会显示高亮，接着输入内容后再定位这步
area=driver.find_element_by_css_selector('div.CodeMirror-scroll > div:nth-child(2)')  
ActionChains(driver).move_to_element(menu).send_keys('dgfdhfgghkjhljklk;kjfghfhfh').perform()

# 提交
driver.find_element_by_class_name('submit_btn').click()






