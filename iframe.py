from selenium import webdriver
import time

# 安居客

driver = webdriver.Chrome()
# 打开登录页面
driver.get("https://login.anjuke.com/login/form")

# 因为iframe 的关系
# 输入bing网址后，搜索 python selenium api 找到WebDriver API （下面是直接进入的网址）
#  http://selenium-python.readthedocs.io/api.html?highlight=iframe  （搜索switch_to 找到switch_to_frame）
#  使用 iframe 的id 找到iframe 
# <iframe class="iframe-login-ifm" id="iframeLoginIfm" src="https://login.anjuke.com/login/iframeform?style=1&amp;forms=11&amp;third_parts=111&amp;other_parts=111&amp;history=aHR0cDovL3d3dy5hbmp1a2UuY29t&amp;check_bind_phone=1&amp;t=1537671143079" frameborder="0" scrolling="no"></iframe>

driver.switch_to_frame("iframeLoginIfm")
# 输入用户名
driver.find_element_by_id('phoneIpt').send_keys('18791042625')


# 输入密码


