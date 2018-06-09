from selenium import webdriver


driver = webdriver.Chrome()

driver.maximize_window()     # 最大化窗口

driver.get('http://www.baidu.com')     # 打开百度网页

driver.find_element_by_link_text('新闻').click()      # 打开新闻链接

driver.back()     # 后退

driver.forward()   # 前进

driver.refresh()    # 刷新


driver.minimize_window()   # 最小化窗口

driver.close()            # 关闭