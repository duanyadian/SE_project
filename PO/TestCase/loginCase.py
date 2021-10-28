from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from PO.BasePage.loginPage import loginPage

login = [["","654321","账号不能为空"],["test","123456","用户名不正确。"],
         ["admin","","密码不能为空"],["admin","654321","用户名或密码不正确"],["admin","123456","用户中心"]]

class TestUser(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,pwd,expected",login)
    def test_user_login(self,username,pwd,expected):

        # 把用例层面实例的driver传到loginPage中
        self.login = loginPage(self.driver)
        # 输入账号密码并登录
        self.login.login(username,pwd)

        if username == "admin" and pwd == "123456":
            # 等待页面加载
            WebDriverWait(self.driver, 3).until(EC.title_is(expected))
            # 验证是否登录成功，根据当前页面标题进行判断
            assert self.driver.title == expected
        else:
            # 等待页面加载
            WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            # 验证报错信息是否正确
            assert alert.text == expected
            alert.accept()