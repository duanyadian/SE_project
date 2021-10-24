from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Browser_init():
    # 使用构造方法，初始化driver变量
    def __init__(self,driver):
        self.driver = driver

    # 元素定位+等待
    def locate_ele(self,locator,time=3):
        wait = WebDriverWait(self.driver,time)
        ele = wait.until(EC.presence_of_element_located(locator))
        return ele

    # 清空输入文本
    def clear_text(self,locator):
        self.locate_ele(locator).clear()

    # 元素输入文本
    def my_sendKeys(self,locator,text):
        self.locate_ele(locator).send_keys(text)

    # 元素点击
    def my_click(self,locator):
        self.locate_ele(locator).click()