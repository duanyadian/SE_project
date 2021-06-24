from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from util import util


class TestUserLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.166.66.25:8080/dyd/user/login")
        self.driver.maximize_window()

    # 测试用户登录，验证码错误
    def test_user_login_code_error(self):
        username = "admin"
        pwd = "123456"
        captcha = "6666"
        expected = "验证码不正确"

        # 输入用户名
        self.driver.find_element(By.NAME,"user").send_keys(username)
        # 输入密码
        self.driver.find_element(By.NAME,"pwd").send_keys(pwd)
        # 输入验证码
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME,"btn").click()
        # 等待提示
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        sleep(2)
        # 验证报错信息
        assert alert.text == expected
        alert.accept()

    # 测试用户登录成功
    def test_user_login_OK(self):
        # 使用工具栏自动生成用户名
        username = util.gen_random_str()
        pwd = "123456"
        # 通过在线api自动识别验证码
        captcha = ""
        expected = "您好 admin , 欢迎回来"

        # 清空输入框后，重新输入用户名
        self.driver.find_element(By.NAME,"user").clear()
        self.driver.find_element(By.NAME,"user").send_keys(username)
        # 清空输入框后，重新输入密码
        self.driver.find_element(By.NAME,"pwd").clear()
        self.driver.find_element(By.NAME,"pwd").send_keys(pwd)
        # 清空验证码
        self.driver.find_element(By.NAME,"captcha").clear()
        # 自动识别验证码
        captcha = util.get_code(self.driver,"captcha")
        # 输入验证码
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME,"btn").click()

        sleep(3)

        # 验证是否登录成功
        assert self.driver.find_element(By.CLASS_NAME,"hidden-xs") == expected

        sleep(2)
        # 关闭浏览器
        self.driver.quit()