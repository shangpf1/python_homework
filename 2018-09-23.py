#  QQ邮箱自动登录

from selenium import webdriver

#  Chrome浏览器驱动
driver = webdriver.Chrome()

# 打开邮箱登录页面
driver.get("https://mail.qq.com/")

# iframe 的使用  找到iframe的ID
# <iframe id="login_frame" name="login_frame" height="100%" scrolling="no" width="100%" frameborder="0" src="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&amp;appid=522005705&amp;daid=4&amp;s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&amp;style=25&amp;low_login=1&amp;proxy_url=https://mail.qq.com/proxy.html&amp;need_qr=0&amp;hide_border=1&amp;border_radius=0&amp;self_regurl=http://zc.qq.com/chs/index.html?type=1&amp;app_id=11005?t=regist&amp;pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&amp;css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input24e6b9.css"></iframe>
driver.switch_to_frame("login_frame")

# 用户、密码及登录按钮
driver.find_element_by_id("u").send_keys("208418427")
driver.find_element_by_xpath('//*[@id="p"]').send_keys("15029946654")
driver.find_element_by_id("login_button").click()


# 备注：如果定位不了，可以用xpath,还是不行的话，可能是因为iframe的问题
# 搜索 python selenium api 找到webdriver API 查找 switch_to 看相关语法