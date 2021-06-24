from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from util import util

class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.166.66.25:8080/dyd/user/register")
        self.driver.maximize_window()

    # 测试登录验证码错误
    def test_register_code_error(self):
        username = "duan"
        email = "123@qq.com"
        pwd = "123456"
        confirmPwd = "123456"
        captcha = "8888"
        expected = "验证码不正确"

        self.driver.find_element(By.NAME,"username").send_keys(username)
        self.driver.find_element(By.NAME,"email").send_keys(email)
        self.driver.find_element(By.NAME,"pwd").send_keys(pwd)
        self.driver.find_element(By.NAME,"confirmPwd").send_keys(confirmPwd)
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        self.driver.find_element(By.CLASS_NAME,"btn").click()
        return
