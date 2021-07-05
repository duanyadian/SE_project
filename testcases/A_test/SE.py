from time import sleep

from selenium import webdriver

# 以面向对象的形式，写个class类
class Test(object): # 继承object
    def __init__(self): # 初始化
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()

    # 定义方法，通过id定位
    def test_id(self):
        self.driver.find_element_by_id("kw").send_keys("功能测试")
        self.driver.find_element_by_id("su").click()
        self.driver.find_element_by_name("wd").clear()
        elem = self.driver.find_element_by_id("su")
        elem.send_keys("接口测试")
        elem.click()

    # 通过name定位
    def test_name(self):
        self.driver.find_element_by_name("wd").send_keys("性能测试")
        self.driver.find_element_by_name("wd").click()

    # 通过classname定位
    def test_ClassName(self):
        self.driver.find_element_by_class_name("s_ipt").clear()
        self.driver.find_element_by_class_name("s_ipt").send_keys("安全测试")
        self.driver.find_element_by_class_name("bg").click()
    # 通过xpath定位
    def test_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').clear()
        elem2 = self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("冒烟测试")
        self.driver.find_element_by_xpath('//*[@id="su"]').click()

    # 通过link链接文本定位
    def test_LinkText(self):
        self.driver.find_element_by_link_text("百度首页").click()
        # self.driver.find_elements_by_link_text("百度首页")[0].click()

    # 通过CSS_Selector定位
    def test_CssSelector(self):
        self.driver.find_element_by_css_selector("#kw").send_keys("软件测试工程师")
        self.driver.find_element_by_css_selector("#su").click()

    # # 通过tag标签定位
    # def test_Tag(self):
    #     ent = self.driver.find_elements_by_tag_name("input")
    #     ent[1].send_keys("测开")
    #     ent[1].click()
    #     print(ent)

    # 通过部分链接文本定位
    def test_PartLinkText(self):
        ele = self.driver.find_elements_by_partial_link_text("度")[1].click()
        print(ele)


if __name__ == "__main__":
    case = Test()
    case.test_id()
    case.test_name()
    case.test_ClassName()
    case.test_xpath()
    case.test_LinkText()
    case.test_PartLinkText()
    case.test_CssSelector()
    case.test_Tag()
    case.test_Class()

    sleep(5)