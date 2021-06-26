from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from util import util
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.166.66.25:8080/dyd/user/register")
        self.driver.maximize_window()

    # 验证注册时用户名为空
    def test_user_register_username(self):
        username = ""
        email = util.gen_random_str() + "@qq.com"
        pwd = "123456"
        confirmPwd = "123456"
        captcha = "6666"
        expected = "用户名不能为空"

        # 输入用户名
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 输入邮箱
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 输入密码
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 输入确认密码
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 输入验证码
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是为”用户名不能为空“
        assert alert.text == expected
        alert.accept()

    # 验证注册时邮箱为空
    def test_user_register_email(self):
        username = "dyd"
        email = ""
        pwd = "123456"
        confirmPwd = "123456"
        captcha = "6666"
        expected = "邮箱不能为空"

        # 清空输入框，并重新输入用户名
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 清空邮箱，并重新输入邮箱
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 清空输入框，并重新输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框，并重新输入确认密码
        self.driver.find_element(By.NAME, "confirmPwd").clear()
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 清空并重新输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是为”邮箱不能为空“
        assert alert.text == expected
        alert.accept()

    # 验证注册时密码为空
    def test_user_register_pwd(self):
        username = "dyd"
        email = util.gen_random_str() + "@qq.com"
        pwd = ""
        confirmPwd = "123456"
        captcha = "6666"
        expected = "密码不能为空"

        # 清空输入框，并重新输入用户名
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 清空邮箱，并重新输入邮箱
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 清空输入框，并重新输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框，并重新输入确认密码
        self.driver.find_element(By.NAME, "confirmPwd").clear()
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 清空并重新输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是为”密码不能为空“
        assert alert.text == expected
        alert.accept()

    # 验证注册时确认密码为空
    def test_user_register_Confirmpwd(self):
        username = "dyd"
        email = util.gen_random_str() + "@qq.com"
        pwd = "123456"
        confirmPwd = ""
        captcha = "6666"
        expected = "确认密码不能为空"

        # 清空输入框，并重新输入用户名
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 清空邮箱，并重新输入邮箱
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 清空输入框，并重新输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框，并重新输入确认密码
        self.driver.find_element(By.NAME, "confirmPwd").clear()
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 清空并重新输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是为”确认密码不能为空“
        assert alert.text == expected
        alert.accept()

    # 验证注册时两次密码不一致
    def test_user_register_different(self):
        # 使用util工具类自动生成用户名
        username = "dyd"
        email = util.gen_random_str() + "@qq.com"
        pwd = "123456"
        confirmPwd = "123"
        captcha = "6666"
        expected = "两次输入密码不一致"

        # 清空输入框，并重新输入用户名
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 清空邮箱，并重新输入邮箱
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 清空输入框，并重新输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 不清空，使用之前的确认密码
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 清空并重新输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是为”两次输入密码不一致“
        assert alert.text == expected
        alert.accept()

    # 测试注册验证码错误
    def test_register_code_error(self):
        username = "admin"
        email = util.gen_random_str() + "@qq.com"
        pwd = "123456"
        confirmPwd = "123456"
        captcha = "8888"
        expected = "验证码不正确"

        # 清空输入框，并重新输入用户名
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 清空邮箱，并重新输入邮箱
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 清空输入框，并重新输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框，并重新输入确认密码
        self.driver.find_element(By.NAME, "confirmPwd").clear()
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 清空并重新输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击【注册】
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver,3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”验证码不正确“
        assert alert.text == expected
        alert.accept()

    # 验证注册成功
    def test_user_register_OK(self):
        # 使用util工具类自动生成用户名
        username = util.gen_random_str()
        email = util.gen_random_str() + "@qq.com"
        pwd = "123456"
        confirmPwd = "123456"
        # 通过在线api自动识别验证码
        captcha = ""
        expected = "注册成功，点击确定进行登录。"

        # 清空输入框，并重新输入用户名
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys(username)
        # 清空邮箱，并重新输入邮箱
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(email)
        # 清空输入框，并重新输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框，并重新输入确认密码
        self.driver.find_element(By.NAME, "confirmPwd").clear()
        self.driver.find_element(By.NAME, "confirmPwd").send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, "captchaimg")
        # 清空并重新输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME, "btn").click()

        # 等待alert弹框出现
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证是否注册成功
        assert alert.text == expected
        alert.accept()

        sleep(1)
        # 关闭浏览器
        self.driver.quit()