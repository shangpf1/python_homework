# 执行JavaScript语法

#如果我们想要将下面的网站的标记的时间改为我们自己想要的时间，不需要手动输入而是让它自动执行代码达到我们的要求，该怎么做呢？

from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.ctrip.com/')
start_date = '2019-01-28'

js_script ='document.querySelector("#HD_CheckIn").value = "{}"'.format(start_date)

print(js_script)
driver.execute_script(js_script)



#  视图滚动
# document.getElementById('tables-responsive').scrollIntoView()


# 和上面的是同样的道理，不需要手动输入日期直接用代码执行即可

# from selenium import webdriver

# driver = webdriver.Chrome()

# driver.get('https://kyfw.12306.cn/otn/index/init')

# driver.execute_script('document.querySelector("#train_date").value = "2019-02-01"')