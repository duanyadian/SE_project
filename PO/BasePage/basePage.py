class Browser_init():
    def __init__(self,driver):
        self.driver = driver

    # 加载项目地址
    def getURL(self,url):
        self.driver.get(url)

    # 元素定位
    def locate_ele(self,locator):
        ele = self.driver.find_element(*locator)
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