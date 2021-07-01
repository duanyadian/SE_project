from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait # 显性等待

class TestArticleDel(object):
    def __init__(self,login):
        self.login = login

    # 测试删除单条文章
    def test_del_one_article(self):
        # 展开文章菜单
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 进入文章管理页面
        sleep(1)
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        # 统计删除前文章总数
        article_num = len(self.login.driver.find_elements(By.CLASS_NAME,"jp-actiontr"))
        # 定义鼠标悬停的元素
        link = self.login.driver.find_element(By.XPATH,
                                              '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')
        # 模拟鼠标悬停
        ActionChains(self.login.driver).move_to_element(link).perform()
        # 操作悬停后出现的元素，(删除文章)
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[3]')\
            .click()
        sleep(1)
        # 统计删除后的文章总数
        article_num1 = len(self.login.driver.find_elements(By.CLASS_NAME,"jp-actiontr"))
        # 断言,删除前文章总数等于删除后文章数加一
        assert article_num == article_num1 + 1

    # 测试删除所有文章
    def test_del_all_article(self):
        expected = "确定要删除该文章吗？删除后不可恢复"
        # 点击文章管理菜单
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        # 勾选选中全部文章
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/th[1]/input')\
            .click()
        # 点击【批量删除】
        self.login.driver.find_element(By.ID,"batchDel").click()

        # 等待弹窗提示出现
        WebDriverWait(self.login.driver,5).until(EC.alert_is_present())
        # 获取弹框文本信息
        alert = self.login.driver.switch_to.alert
        # 断言判断，提示信息是否正确
        assert alert.text == expected
        # 点击【确定】
        alert.accept()

        sleep(1)
        # 获取删除后的文章
        article_num = self.login.driver.find_elements(By.CLASS_NAME,"jp-actiontr")
        # 断言判断，删除后的文章总数应为零
        assert len(article_num) == 0

        sleep(1)
        #关闭浏览器
        self.login.driver.quit()