import csv

import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data():
    lst = []
    with open("my_data.csv","r",encoding='UTF-8') as j:    # 只读模式打开json文件
        data = csv.reader(j)    # 将json转换为字典
        for row in data: # 遍历字典
            lst.extend(row)   #将数据以元组形式添加到lst中
    return lst  # 返回lst

class TestUser(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.166.66.22:8080/article/2")

    @pytest.mark.parametrize("content",get_data()) # 调用excel文件中的数据
    def test_user_login_Error(self,content):
        comment = content
        expected = "评论失败：验证码错误"

        self.driver.find_element(By.NAME, "content").clear()
        self.driver.find_element(By.NAME, "content").send_keys(comment)
        self.driver.find_element(By.NAME, "captcha").send_keys(666)
        self.driver.find_element(By.XPATH, "//button").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证报错信息是否正确
        assert alert.text == expected
        alert.accept()