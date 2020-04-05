# 微博搜索结果页面爬虫实践

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://s.weibo.com/")
driver.maximize_window()

# 在输入框输入web自动化，且点击搜索按钮
driver.find_element_by_css_selector('#pl_homepage_search > div > div.searchbox > div > input[type="text"]').send_keys('web自动化')
driver.find_element_by_class_name('s-btn-b').click()

# 选择高级搜索按钮，选择原创，点击搜索微博
driver.find_element_by_xpath('//*[@id="pl_feedtop_top"]/div[3]/a').click()
driver.find_element_by_id('radio03').click()
driver.find_element_by_link_text('搜索微博').click()

# 定位一条信息（此作者发了8条信息）
eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')

for ele in eles:
    title = ele.find_element_by_css_selector('p[class="txt"]').text
    username = ele.find_element_by_css_selector('a[class="name"]').text
    time = ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text
    source = ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text
    coll = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(1)').text
    coll_num = coll.split('收藏')[1]
    forward = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text
    forward_num = forward.split('转发')[1]
    comment = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(3)').text
    comment_num = comment.split('评论')[1]
    like = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(4)').text
    print(title,username,time,source,coll_num,forward_num,comment_num,like)


