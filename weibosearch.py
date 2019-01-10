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



# 搜索结果如下：
DevTools listening on ws://127.0.0.1:53750/devtools/browser/eae5609a-9fe8-4d8d-837e-f78b08fc4ad6
发布了头条文章：《web自动化测试神器——selenium家族介绍》 IT技术 Oweb自动化测试神器——selenium家族介绍 源码时代 01月07日 11:39 01月07日 11:39   1
#新浪看点# web自动化测试神器——selenium家族介绍Oweb自动化测试神器——selenium家族介绍 源码时代 01月07日 11:33 01月07日 11:33   1
web自动化测试从入门到持续集成@慕课网 原创_慕课网_手记 Oweb自动化测试从入门到持续集成@慕课网 原创_慕课网_手记 二姑娘change 01月03日 16:17 01月03日 16:17

发表了博文《软件测试特训营基础到就业班，系统测试，WEB测试，UFT与Selenium自动化测试，LR性能测试视频课程》软件测试特训营基础到就业班，系统测试，WEB测试，UFT
与Selenium自动化O软件测试特训营基础到就业班，系统测试，WEB测试，UFT与Selenium自动化测试，LR性能测试视频课程 爱编程168 2018年12月31日 20:00 2018年12月31日 20:00
#O网页链接# 【全栈增长工程师实战之功能测试与持续集成】编写自动化测试我们就可以用Selenium来做自动化测试。这是ThoughtWorks出品的一个强大的基于浏览器的开源自
动化测试工具，它通常用来编写Web 应用的自动化测试......O网页链接 51Testing软件测试网 2018年12月29日 09:31 2018年12月29日 09:31    1
web自动化_环境安装配置 Oweb自动化_环境安装配置 难合称i 2018年12月26日 14:21 2018年12月26日 14:21    1
发表了博文《1分钟入门接口自动化框架Karate》交流软件测试最新技术，获取软测工具、资料，来交流互助群617089523，进群暗号：IT王者!在这篇文章中，我们将介绍一下开源的Web-API自动化测O1分钟入门接口自动化框架Karate IT科技青年 2018年12月25日 20:30 2018年12月25日 20:30
好的测试要会功能，接口，web自动化，app自动化，loadrunner性能，再升级就是会修改代码中的bug✌ 小嵘儿-哈哈哈 2018年12月23日 11:59 2018年12月23日 11:59 
