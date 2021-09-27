import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data():
    lst = []
    with open("my_data.json","r",encoding='UTF-8') as j:    # 只读模式打开json文件
        dict_data = json.loads(j.read())    # 将json转换为字典
        for i in dict_data: # 遍历字典
            lst.append(tuple(i.values()))   #将数据以元组形式添加到lst中
    return lst  # 返回lst

class TestUser(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.166.66.22:8080/user/login")

    @pytest.mark.parametrize("username,pwd,expected",get_data())    # 调用json数据
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
        self.driver.quit()