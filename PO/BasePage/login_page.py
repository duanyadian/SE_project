from selenium.webdriver.common.by import By

# 抽出定位和元素属性值
class LoginPage():
    # 使用构造方法，初始化driver变量
    def __init__(self,driver):
        self.driver = driver

    user_input = (By.NAME, "user")
    pwd_input = (By.NAME, "pwd")
    login_btn = (By.CLASS_NAME, "btn")

    #元素操作
    # 1、用户名清空和输入
    def input_userName(self,username):
        # self.driver.find_element(*LoginPage.user_input).clear()
        # self.driver.find_element(*LoginPage.user_input).send_keys(username)
        self.driver.clear_text()
        self.driver.my_sendKeys(*LoginPage.user_input,username)
    # 2、密码清空和输入
    def input_userPwd(self,passwd):
        # self.driver.find_element(*LoginPage.pwd_input).clear()
        # self.driver.find_element(*LoginPage.pwd_input).send_keys(passwd)
        self.driver.clear_text()
        self.driver.my_sendKeys(*LoginPage.user_input,passwd)
    # 3、点击登录按钮
    def login_btnClick(self):
        # self.driver.find_element(*LoginPage.login_btn).click()
        self.driver.my_click()

    # 绑定业务函数，非必需，根据业务判断是否需要
    def login(self,user,pwd):
        self.input_userName(user)
        self.input_userPwd(pwd)
        self.login_btnClick()

