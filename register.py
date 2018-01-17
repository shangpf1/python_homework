'''
CNode url= http://118.31.19.120:3000/
注册邮件不会发
远程链接到数据库改数据
作业要求：1、测试用例，用代码注释的方法；2、至少用三个测试用例 3、加分：把测试用例放到csv或者excel 文件里读取
遗留问题
'''
from selenium import webdriver
# import time
drvier = webdriver.Chrome(executable_path="./chromedriver")

# 打开Node注册页面
drvier.get("http://118.31.19.120:3000/")

# 注册 register
registerXpath = "/html/body/div[1]/div/div/ul/li[5]/a"
registerXpath = drvier.find_element_by_xpath(registerXpath)
registerXpath.click()

# 输入用户名
usermaneinput = "loginname"
username=drvier.find_element_by_id(usermaneinput)
username.send_keys('lifei123')

#输入密码
pwdinput = "pass"
pwd=drvier.find_element_by_id(pwdinput)
pwd.send_keys('123456')

#输入确认密码
repwdinput = "re_pass"
repwd=drvier.find_element_by_id(repwdinput)
repwd.send_keys('123456')

#输入邮箱地址
emailinput = "email"
email=drvier.find_element_by_id(emailinput)
email.send_keys('208418427@163.com')

#点击注册按钮
registerBot = "span-primary" 
drvier.find_element_by_class_name("span-primary")
drvier.click()

# time.sleep(6)


