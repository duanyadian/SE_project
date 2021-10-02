import pytest
import allure
from selenium import webdriver
from util import util

# def test_baidu():
#     driver = webdriver.Chrome()
#     driver.get("http://www.baidu.com")
#     try:
#         driver.find_element_by_id("xxx")
#     except Exception as e:
#         img = driver.get_screenshot_as_png()
#         allure.attach(img,"失败截图",allure.attachment_type.PNG)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu(init_driver):
    init_driver.get("http://baidu.com")
    init_driver.find_element(By.CLASS_NAME, "123").click()

logging = util.get_logger()
@allure.title("用例执行失败时截图并记录日志")
def test_jpress(init_driver):
    # driver = webdriver.Chrome()
    init_driver.get("http://192.166.66.22:8080/admin/login")
    init_driver.find_element(By.NAME, "user").send_keys("admin")
    init_driver.find_element(By.NAME, "pwd").send_keys("123456")
    init_driver.find_element(By.NAME, "captcha").send_keys(8888)
    init_driver.find_element(By.CLASS_NAME, "btn错误的登录按钮元素").click()
    img = init_driver.get_screenshot_as_png()
    allure.attach(img,"失败截图",allure.attachment_type.PNG)
    WebDriverWait(init_driver, 3).until(EC.alert_is_present())
    alert = init_driver.switch_to.alert
    assert alert.text == "登录失败"

