'''
selenium 元素定位的8中方法
注：其中by_tag_name 很少用到，标签的意思（input）,若页面比较简单时可以用

'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Learn-python\python_homework\chromedriver.exe")

driver.get("http://www.baidu.com")

#driver.find_element_by_id('kw').send_keys('helloworld').click()

#driver.find_element_by_name('wd').send_keys('helloworld').click()

#driver.find_element_by_xpath('//*[@id="kw"]').send_keys('helloworld').click()

#driver.find_element_by_link_text('新闻').click()

#driver.find_element_by_partial_link_text('新').click()

#driver.find_element_by_class_name('s_ipt').send_keys('helloworld').click()

driver.find_element_by_css_selector('#kw').send_keys('helloworld').click()