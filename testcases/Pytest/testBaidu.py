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

logger = util.get_logger()
# pytest.mark.parametrize("username,pwd,capt",["admin","123456","8888"])
def test_baidu():
    driver = webdriver.Chrome()
    driver.get("http://192.166.66.22:8080/admin/login")
    driver.find_element(By.NAME, "user").send_keys("admin")
    driver.find_element(By.NAME, "pwd").send_keys("123456")
    driver.find_element(By.NAME, "captcha").send_keys(8888)
    driver.find_element(By.CLASS_NAME, "btn").click()
    WebDriverWait(driver, 3).until(EC.url_contains("admin/index"))
    try:
        assert driver.title == "JPress后台"
    except Exception as e:
        img = driver.get_screenshot_as_png()
        allure.attach(img,"失败截图",allure.attachment_type.PNG)
        log = logger.error("报错信息:%s", "无法登录，找不到登录按钮", exc_info=1)
        allure.attach.file(driver.get_log(log), "失败日志", allure.attachment_type.TEXT)
