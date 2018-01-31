
# 创建一个登陆CNode论坛的类和方法，成功登陆此论坛

# class Myclass:
#     i = 123
#     def f(self):
#         print(self.i)

# my = Myclass()
# my.f()


from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://118.31.19.120:3000/signin")

class LoginPage:
    username_id = "name"
    passwd_id = "pass"
    login_btn_className = "span-primary"


    def user_login(self,username,passwd):
        driver.find_element_by_id(self.username_id).send_keys(username)
        driver.find_element_by_id(self.passwd_id).send_keys(passwd)
        driver.find_element_by_class_name(self.login_btn_className).click()


login = LoginPage()
login.user_login('helloworld','123456')