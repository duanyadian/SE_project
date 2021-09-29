import pytest
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data(): # 定义一个获取数据的函数
    filename = "my_data.xlsx" # 定义数据文件
    wb = xlrd.open_workbook(filename)   # 打开文件
    sheet = wb.sheet_by_index(0)    # 使用索引方式获得文件中的第一个sheet
    rows = sheet.nrows  # 获取行
    cols = sheet.ncols  # 获取列
    lst = []
    for row in range(rows): # 遍历行
        for col in range(cols): # 遍历列
            cell_data = sheet.cell_value(row,col)   # 获取单元格中的数据
            lst.append([cell_data])   # 将单元格中的数添加到列表中

    return lst  # 返回list列表

class TestUser(object):
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://192.166.66.22:8080/article/2")

    @pytest.mark.parametrize("content",get_data()) # 调用excel文件中的数据
    def test_user_login_Error(self,content):
        comment = content
        expected = "评论失败：验证码错误"

        self.driver.find_element(By.NAME, "content").clear()
        self.driver.find_element(By.NAME, "content").send_keys(comment)
        self.driver.find_element(By.NAME, "captcha").send_keys(666)
        self.driver.find_element(By.XPATH, "//button").click()
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # 验证报错信息是否正确
        assert alert.text == expected
        alert.accept()

@pytest.mark.parametrize("value",get_data())    # 调用excel数据
def test_read(value):
    print(value)

if __name__ == '__main__':
    pytest.main(["-vs","test_excel.py"])