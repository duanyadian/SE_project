from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_mouse(self):
        self.driver.get("http://www.sahitest.com/demo/clicks.htm")
        cli = self.driver.find_element(By.XPATH,"//input[3]")
        ActionChains(self.driver).click(cli).perform() # 单击鼠标左键
        dblcli = self.driver.find_element(By.XPATH,"//input[2]")
        ActionChains(self.driver).double_click(dblcli).perform() # 双击鼠标左键
        ActionChains(self.driver).click_and_hold(cli).perform() # 按照鼠标左键不松手
        sleep(2)
        ActionChains(self.driver).release(cli).perform() # 松开鼠标
        cliR = self.driver.find_element(By.XPATH,"//input[4]")
        ActionChains(self.driver).context_click(cliR).perform() # 单击鼠标右键

        sleep(2)

    def test_dragdrop(self):
        self.driver.get("http://www.sahitest.com/demo/dragDropMooTools.htm")
        sourse = self.driver.find_element(By.ID,"dragger")
        target = self.driver.find_element(By.XPATH,'//div[@class="item"][1]')
        print(target.rect)
        ActionChains(self.driver).drag_and_drop(sourse,target).perform() # 将元素拖拽至某处
        sleep(1)
        ActionChains(self.driver).drag_and_drop_by_offset(sourse,137,115).perform() # 将元素拖拽至指定坐标

    def test_keyboard(self):
        self.driver.get("https://www.bilibili.com/")
        kb = self.driver.find_element(By.CLASS_NAME,"nav-search-keyword")
        kb.send_keys("Web自动化测试")
        kb.send_keys(Keys.CONTROL,"a") # 按Ctrl+A键
        sleep(1)
        kb.send_keys(Keys.CONTROL,"x") # 按Ctrl+X键
        sleep(1)
        kb.send_keys(Keys.CONTROL,"v") # 按Ctrl+V键
        sleep(1)
        kb.send_keys(Keys.CONTROL,"a") # 按Ctrl+A键
        kb.send_keys(Keys.DELETE) # 按Delete键
        sleep(1)
        # 模拟键盘按下和松开通常key_down后需要key_up，否则可能影响后面的操作
        ActionChains(self.driver).key_down(Keys.CONTROL,kb).send_keys("测试").key_up(Keys.CONTROL).perform()

        ele = self.driver.find_element(By.LINK_TEXT,"热门")
        ActionChains(self.driver).move_to_element(ele).perform() # 将鼠标移动至指定元素上
        sleep(2)
        print(self.driver.find_element(By.ID,"reportFirst1").rect)
        ActionChains(self.driver).move_by_offset(139.6666717529297,263).perform() # 将鼠标移动至坐标处
        sleep(2)
        ActionChains(self.driver).move_to_element_with_offset(ele,523,305).perform() # 将鼠标移动至距离指定位置的距离
if __name__ == '__main__':
    test = TestCase()
    # test.test_mouse()
    # test.test_dragdrop()
    test.test_keyboard()
