from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.bilibili.com/")
        self.driver.maximize_window()

    def test_sleep(self):
        ele = self.driver.find_element_by_link_text("知识")
        sleep(2) # 线程阻塞，blacking wait 2s
        ele.click()
        sleep(3)
        self.driver.quit()

    def test_implicitly(self):
        self.driver.implicitly_wait(3) # 等待3秒后执行下一步
        self.driver.find_element_by_class_name("nav-search-keyword").send_keys("测开")
        self.driver.find_element_by_class_name("nav-search-btn").click()
        self.driver.quit()

    def test_WebDriverWait(self):
        handle = self.driver.current_window_handle  # 获取当前窗口句柄
        self.driver.find_element_by_link_text("热门").click()
        handles = self.driver.window_handles # 获取当前所有窗口
        for newhandle in handles: # 对窗口进行遍历
            if newhandle != handle: # 判断当前窗口是否为新窗口
                self.driver.switch_to.window(newhandle) # 切换到新打开的窗口
        WebDriverWait(self.driver, 3).until(expected_conditions.title_is("哔哩哔哩热门"),message="页面访问加载错误")
        self.driver.find_element_by_class_name("mask-tips-step").click()
        self.driver.close() # 关闭当前窗口
        self.driver.switch_to.window(handles[0]) # 切换窗口

if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicitly()
    case.test_WebDriverWait()