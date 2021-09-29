import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data():
    lst = []
    with open("my_data.yaml","r",encoding='UTF-8') as j:    # 只读模式打开yaml文件
        ym = yaml.load_all(j.read()) # 使用load_all生成迭代器
        for i in ym: # 遍历ym中的数据
            lst.append(tuple(i.values()))   #将数据以元组形式添加到lst中
    return lst  # 返回lst

class TestUser(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.166.66.22:8080/user/login")
        print(get_data())

    @pytest.mark.parametrize("username,pwd,expected",get_data())    # 调用yaml数据
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
        # 等待页面加载
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证报错信息是否正确
        assert alert.text == expected
        alert.accept()