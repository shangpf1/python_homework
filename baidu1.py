from selenium import webdriver
import time

# 百度中登录百度账号

#设置浏览器（谷歌浏览器）
drvier = webdriver.Chrome(executable_path="./chromedriver")


# 打开页面
drvier.get("https://www.baidu.com/")


# 登录
loginXpath='//*[@id="u1"]/a[7]'
loginXpath = drvier.find_element_by_xpath(loginXpath)
loginXpath.click()

time.sleep(3)

# 用户登录
usernameXpath = '//*[@id="TANGRAM__PSP_10__footerULoginBtn"]'
usernamelink = drvier.find_element_by_xpath(usernameXpath)
usernamelink.click()

#输入用户名、密码
phoneXpath = '//*[@id="TANGRAM__PSP_10__userName"]'
passwdXpath = '//*[@id="TANGRAM__PSP_10__password"]'
phoneinput = drvier.find_element_by_xpath(phoneXpath)
passwdinput = drvier.find_element_by_xpath(passwdXpath)

phoneinput.send_keys('12345678905')
passwdinput.send_keys('xxxxxx')

# 点击登录按钮
loginBtnXpath = '//*[@id="TANGRAM__PSP_10__submit"]'
loginBtn = drvier.find_element_by_xpath(loginBtnXpath)
loginBtn.click()



