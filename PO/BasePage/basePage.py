from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser_init():
    def __init__(self,driver):
        self.driver = driver

    # 元素等位+等待
    def locate_ele(self,locator,time=3):
        wait = WebDriverWait(self,locator,time)
        ele = wait.until(EC.presence_of_element_located(locator),message="未找到元素")
        return ele

    # 元素文本清空
    def locate_clear(self,locator):
        self.locate_ele(locator).clear()

    # 元素文本输入
    def locate_input(self,locator,text):
        self.locate_ele(locator).send_keys(text)

    # 元素点击
    def locate_click(self,locator):
        self.locate_ele(locator).click()

