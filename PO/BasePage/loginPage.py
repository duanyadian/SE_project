from selenium.webdriver.common.by import By
from PO.BasePage.basePage import Browser_init

class loginPage(Browser_init):

    # 抽出定位和元素的属性值
    user = (By.NAME, "user")
    pwd = (By.NAME, "pwd")
    btn = (By.CLASS_NAME, "btn")
    url = "http://192.166.66.22:8080/user/login"

    # 加载项目地址
    def user_loginURL(self):
        self.getURL(self.url)

    # 元素操作
    # 清空输入框后输入用户名
    def user_input(self,username):
        self.locate_clear(loginPage.user)
        self.locate_input(loginPage.user,username)
    # 清空输入框后输入密码
    def pwd_input(self,pwd):
        self.locate_clear(loginPage.pwd)
        self.locate_input(loginPage.pwd,pwd)

    # 点击登录按钮
    def btn_click(self):
        self.locate_click(loginPage.btn)

    # 绑定业务函数
    # 对于有关联关系的操作可以进行业务绑定
    def login(self,username,pwd):
        self.user_loginURL()
        self.user_input(username)
        self.pwd_input(pwd)
        self.btn_click()
