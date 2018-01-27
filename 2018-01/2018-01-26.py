'''
selenium_actions使用技巧-实战CNode发帖操作

'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="D:\Learn-python\python_homework\chromedriver")

# 打开CNode论坛页面
driver.get("http://118.31.19.120:3000/signin")

# 输入用户名、密码
driver.find_element_by_id('name').send_keys('helloworld')
driver.find_element_by_id('pass').send_keys('123456')

# 点击登录按钮
driver.find_element_by_class_name('span-primary').click()

#点击发布话题按钮
driver.find_element_by_class_name('span-success').click()

#选择版块
driver.find_element_by_id('tab-value').click()
driver.find_element_by_css_selector('#tab-value > option:nth-child(3)').click()

# 标题
driver.find_element_by_id('title').send_keys('python 学习')

# 写入文本
contentInput = driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre')

#鼠标光标定位
ActionChains(driver).move_to_element(contentInput).click().perform()


contentArea = driver.find_element_by_css_selector('#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code')
ActionChains(driver).move_to_element(contentInput).send_keys('Do you like learn python ?').perform()