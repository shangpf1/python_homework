from selenium import webdriver


# for windows user
# drvier = webdriver.Chrome(executable_path="./chromedriver.exe")
# for mac user

#设置浏览器（谷歌浏览器）
drvier = webdriver.Chrome(executable_path="./chromedriver")


# 打开页面
drvier.get("https://www.baidu.com/")

# #找到贴吧 link
# tieba = drvier.find_element_by_xpath("//*[@id="u1"]/a[5]")

# # link 链接
# tieba = drvier.find_element_by_link_text("贴吧")

# # 部分链接
# tieba = drvier.find_element_by_partial_link_text("贴吧")
# tieba.click()

# baiduserach = drvier.find_element_by_class_name("wd")
# baiduserach.send_keys("helloworld")

baiduserach = drvier.find_element_by_css_selector("#kw")

#找到搜索框元素
# baiduserach =  drvier.find_element_by_id("kw")

#baiduserach =  drvier.find_element_by_name("wd")
# baiduserach.send_keys("helloworld")




# elem = browser.find_element_by_class_name('p')
# elem.send_keys('seleniumhq'+ Keys.RETURN)

# browser.quit() 