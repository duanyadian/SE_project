from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TESTEC(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_dyd(self):
        self.driver.get("https://www.bilibili.com/")
        WebDriverWait(self.driver,3).until(EC.title_is("哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"))
        self.driver.find_element(By.LINK_TEXT,"科技").click()
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for newhandle in handles:
            if newhandle != handle:
                self.driver.switch_to.window(newhandle)
        WebDriverWait(self.driver,2).until(EC.title_contains("科技区"),message="页面加载失败") #
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.LINK_TEXT, '软件应用')))
        WebDriverWait(self.driver,1).until(EC.presence_of_all_elements_located((By.LINK_TEXT,"全部")))
        WebDriverWait(self.driver,4).until(EC.visibility_of_element_located((By.LINK_TEXT,"数码")))
        WebDriverWait(self.driver,5).until(EC.visibility_of_any_elements_located((By.LINK_TEXT,"热门")))
        WebDriverWait(self.driver,2).until(EC.text_to_be_present_in_element((By.PARTIAL_LINK_TEXT,"计算"), "技术"))
        try:
            WebDriverWait(self.driver,3).until(EC.alert_is_present())
        except:
            print("指定时间内未出现弹窗")
    def test_frame(self):
        self.driver.get("http://www.sahitest.com/demo/framesTest.htm")
        frame = self.driver.find_element(By.XPATH,'//frame[2]')
        WebDriverWait(self.driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//frame[2]')))
        try:
            self.driver.switch_to.frame(frame)
        except:
            print("出错啦")
        self.driver.find_element(By.LINK_TEXT,"IFrames Test").click()

    def test_select(self):
        self.driver.get("http://www.sahitest.com/demo/selectTest.htm")
        ele = self.driver.find_element(By.ID,"s1Id")
        se = Select(ele)
        se.select_by_index(2)
        # WebDriverWait(self.driver,3).until(EC.text_to_be_present_in_element_value((By.ID,"s1Id"),"o1"))
        wait = WebDriverWait(self.driver,3)
        # wait.until(EC.element_to_be_selected((By.ID,"id2")))
        ele1 = self.driver.find_element(By.ID,"id3")
        wait.until(EC.element_selection_state_to_be(ele1,"o2"))
        wait.until(EC.element_located_selection_state_to_be((By.ID,"id3"),"o3"))
        # WebDriverWait(self.driver,6).until(EC.invisibility_of_element_located((By.NAME,"keywords")))
        # WebDriverWait(self.driver,5).until(EC.visibility_of((By.LINK_TEXT,"计算机技术")))


if __name__ == '__main__':
    test = TESTEC()
    test.test_dyd()
    test.test_frame()
    test.test_select()
