from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CaseWebEle(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("https://www.bilibili.com/")
        self.driver.get("http://www.sahitest.com/demo/selectTest.htm")
        self.driver.maximize_window()
    def test_webele(self):
        a = self.driver.find_element(By.CLASS_NAME,"nav-search-keyword")
        print(type(a)) # 打印元素类型
        print(a.id)    # 打印元素id
        print(a.size)  # 打印元素宽度和高度
        print(a.rect)  # 打印元素宽高及坐标
        print(a.text)  # 打印元素文本信息
        print(a.tag_name)      # 打印元素的标签名称
        a.send_keys("测试开发")  # 发送文本内容
        print(a.get_attribute("class")) # 获取a元素的calss的值
        print(a.value_of_css_property("font")) # 获取CSS中font的值
        print(a.is_selected())  # 打印是否选中结果
        print(a.is_enabled())   # 打印是否启用结果
        print(a.is_displayed()) # 打印是否显示结果

        a.clear()
        a.click()

    def test_select(self):
        ele = self.driver.find_element(By.ID,"s1Id")
        sel = Select(ele)
        sel.select_by_index(2) # 根据索引选择
        sleep(1)
        sel.select_by_value("o1")  # 根据value值选择
        sleep(1)
        sel.select_by_visible_text("o3") # 根据文本内容选择
        sleep(1)

    def test_deselect(self):
        ele1 = self.driver.find_element(By.ID,"s4Id")
        sel1 = Select(ele1)
        for i in range(6):
            sel1.select_by_index(i)
            sleep(1)
        # sel1.deselect_all() # 反选所有选项
        sel1.deselect_by_index(3) # 根据索引反选
        sleep(1)
        sel1.deselect_by_value("o2val") # 根据value值反选
        sleep(1)
        sel1.deselect_by_visible_text("With spaces") # 根据文本内容反选
        sleep(1)

        for option in sel1.options:
            print(option.text) # 打印所有选项

        self.driver.quit()

if __name__ == '__main__':
    test = CaseWebEle()
    # test.test_webele()
    test.test_select()
    test.test_deselect()