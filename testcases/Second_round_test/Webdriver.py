from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bilibili.com/")
        self.driver.maximize_window()
    def test_attr(self):
        print(self.driver.name) # 打印浏览器名称
        print(self.driver.title) # 打印当前页面标题
        b = self.driver.current_url # 打印当前访问的URL
        print(self.driver.current_window_handle)  # 打印当前访问的句柄
        print(self.driver.page_source)
        # self.driver.close()
        sleep(1)
    def test_method(self):
        self.driver.find_element(By.LINK_TEXT,"知识").click()
        self.driver.back() # 后退
        self.driver.forward() # 前进
        self.driver.refresh() # 刷新页面
        sleep(1)
        self.driver.find_element(By.LINK_TEXT,"热门").click()
        win = self.driver.window_handles # 获取所有句柄(即每个tab)

        while 1:
            for w in win:
                self.driver.switch_to.window(w) # 切换窗口
                sleep(5)

            self.driver.quit()


if __name__ == "__main__":
    case = TestCase()
    case.test_attr()
    case.test_method()