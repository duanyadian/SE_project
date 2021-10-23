from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure

login = [["","654321","账号不能为空"],["test","123456","用户名不正确。"],
         ["admin","","密码不能为空"],["admin","654321","用户名或密码不正确"],["admin","123456","用户中心"]]


@allure.feature("Jpress后端测试")
class TestUser(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.166.66.22:8080/user/login")
        self.logger.info("登录测试")

    # 测试用户登录信息错误
    @allure.story("这是用户登录测试用例")
    @allure.description("登录平台-测试")
    @pytest.mark.parametrize("username,pwd,expected",login)
    def test_user_login_Error(self,username,pwd,expected):
        user = username
        pwd = pwd
        expected = expected

        # 清空输入框后输入用户名
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(user)
        # 清空输入框后输入密码
        self.driver.find_element(By.NAME, "pwd").clear()
        self.driver.find_element(By.NAME, "pwd").send_keys(pwd)
        # 点击【登录】
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        if user == "admin" and pwd == "123456":
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
            self.logger.debug("登录失败，用户名或密码输出有误！")
            alert.accept()

    sleep(2)
    @allure.story("文章管理测试用例")
    @allure.title("查看文章列表")
    @allure.step("步骤1：进入文章列表")
    def test_article_list(self):
        expected = "http://192.166.66.22:8080/ucenter/article"
        self.driver.find_element(By.XPATH,'//span[contains(text(),"我的文章")]').click()
        self.driver.find_element(By.LINK_TEXT,"文章列表").click()
        WebDriverWait(self.driver, 2).until(EC.url_contains("/ucenter/article"))
        assert self.driver.current_url == expected

    @allure.story("文章管理测试用例")
    @allure.title("查看文章详情")
    @allure.step("步骤2：查看文章详情")
    @allure.severity(severity_level="critical")
    def test_Look_article(self):
        expected = "一个小测试"
        handle = self.driver.current_window_handle  # 获取当前窗口句柄
        self.driver.find_element(By.LINK_TEXT, "一个小测试").click()
        handles = self.driver.window_handles  # 获取所有窗口句柄
        for newhandle in handles:  # 对窗口进行遍历
            if newhandle != handle:  # 判断当前窗口是否为新窗口
                self.driver.switch_to.window(newhandle)  # 切换到新打开的窗口
        WebDriverWait(self.driver, 2).until(EC.title_is(expected))
        assert self.driver.title == expected
        # 关闭浏览器
        self.driver.quit()

@allure.feature("Jpress前端测试")
class TestBlog(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.166.66.22:8080/")
        self.logger.info("博客访问测试")

    @allure.title("查看博客详情")
    @pytest.mark.skipif(reason="刻意跳过此用例")
    def test_details(self):
        expected = "一个小测试"
        self.driver.find_element(By.CLASS_NAME,"bh-card-main-title").click()
        WebDriverWait(self.driver, 2).until(EC.url_contains("/article/2"))
        assert self.driver.title == expected
        # 关闭浏览器
        self.driver.quit()

