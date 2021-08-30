from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util

class TestAdminLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.166.66.25:8080/dyd/admin/login")
        self.driver.maximize_window()

    # 测试管理员登录时用户名为空
    def test_admin_login_nameEmpty(self):
        pwd = "123456"
        captcha = "8888"
        expected = "账号不能为空"

        # 输入密码
        self.driver.find_element(By.NAME,"pwd").send_keys(pwd)
        # 输入验证码
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击登录
        self.driver.find_element(By.CLASS_NAME,"btn").click()
        # 等待弹窗提示，3秒后无弹窗则抛出异常
        WebDriverWait(self.driver,3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”账号不能为空“
        assert alert.text == expected
        alert.accept()

    # 测试管理员登录时用户名错误
    def test_admin_login_nameError(self):
        username = "test"
        pwd = "123456"
        # 通过在线api自动识别验证码
        captcha = ""
        expected = "用户名不正确。"

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # 清空输入框后输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver,"captchaImg")
        # 清空输入框后输入验证码
        self.driver.find_element(By.NAME,"captcha").clear()
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        # 等待弹窗提示，3秒后无弹窗则抛出异常
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”用户名不正确。“
        assert alert.text == expected
        alert.accept()

    # 测试管理员登录时密码为空
    def test_admin_login_pwdEmpty(self):
        username = "admin"
        captcha = "8888"
        expected = "密码不能为空"

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # 清空密码
        self.driver.find_element(By.NAME, "pwd").clear()
        # 清空输入框后输入验证码
        self.driver.find_element(By.NAME,"captcha").clear()
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        # 等待弹窗提示，3秒后无弹窗则抛出异常
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”密码不能为空“
        assert alert.text == expected
        alert.accept()

    # 测试管理员登录时密码错误
    def test_admin_login_pwdError(self):
        username = "admin"
        pwd = "654321"
        # 通过在线api自动识别验证码
        captcha = ""
        expected = "用户名或密码不正确"

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # 清空输入框后输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver,"captchaImg")
        # 清空输入框后输入验证码
        self.driver.find_element(By.NAME,"captcha").clear()
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        # 等待弹窗提示，3秒后无弹窗则抛出异常
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”用户名或密码不正确“
        assert alert.text == expected
        alert.accept()

    # 测试管理员登录时验证码为空
    def test_admin_login_captchaEmpty(self):
        username = "admin"
        pwd = "123456"
        expected = "验证码不能为空"

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # 清空输入框后输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框后输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        # 等待弹窗提示，3秒后无弹窗则抛出异常
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”验证码不能为空“
        assert alert.text == expected
        alert.accept()

    # 测试管理员登录时用户名错误
    def test_admin_login_captchaError(self):
        username = "admin"
        pwd = "123456"
        captcha = "8888"
        expected = "验证码不正确，请重新输入"

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # 清空输入框后输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 清空输入框后输入验证码
        self.driver.find_element(By.NAME, "captcha").clear()
        self.driver.find_element(By.NAME, "captcha").send_keys(captcha)
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        # 等待弹窗提示，3秒后无弹窗则抛出异常
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证报错信息是否为”验证码不正确，请重新输入“
        assert alert.text == expected
        alert.accept()

    # 测试管理员登录成功
    def test_admin_login_OK(self):
        username = "admin"
        pwd = "123456"
        # 通过在线api自动识别验证码
        captcha = ""
        expected = "JPress后台"

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        # 清空输入框后输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, "captchaImg")
        # 清空输入框后输入验证码
        self.driver.find_element(By.NAME,"captcha").clear()
        self.driver.find_element(By.NAME,"captcha").send_keys(captcha)
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        # 等待页面加载
        WebDriverWait(self.driver, 3).until(EC.title_is(expected))

        # 验证是否登录成功，根据当前页面标题进行判断
        assert self.driver.title == expected

        # 关闭浏览器
        # self.driver.quit()
