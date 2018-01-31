# 类的构造方法和私有属性

class person:

    # useraname = 'xiaoming'
    # passwd = '123456'
    # email = 'xiaoming@126.com'

   # 构造方法
    def __init__(self,username,passwd,email):
        self.username = username
        self.passwd = passwd
        self.email = email

    def user_register(self):
        print("用户注册：",self.username,self.passwd,self.email)

    def user_login(self):
        print("用户登陆：",self.username,self.passwd)
        print("-----------------------------------------")

p = person('xiaofei','123457','xiaofei@123.com')
p.user_register()
p.user_login()

p1 = person('zhangfei','366666','zhangfei@126.com')
p1.user_register()
p1.user_login()