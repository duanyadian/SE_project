from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestArticle(object):
    def __init__(self,login):
        self.login = login

    # 测试写文章,标题为空
    def test_add_article_TitleEmpoty(self):
        title = ""
        content = "岁月拐走了单纯，人生是越走越复杂，复杂而肤浅"
        expected = "标题不能为空"

        # 展开文章菜单
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 进入写文章页面
        sleep(1)
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        # 填写文章标题
        self.login.driver.find_element(By.ID,'article-title').send_keys(title)
        # 切入iframe框架内
        frame1 = self.login.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(frame1)
        # 填写文章内容
        self.login.driver.find_element(By.XPATH,'/html/body').send_keys(content)
        # 切出iframe框架
        self.login.driver.switch_to.default_content()
        # 点击【发布】按钮
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        # 定位报错信息
        sleep(1)
        loc = (By.CLASS_NAME,"toast-message")
        # 等待弹框出现，6秒内未出现则抛出异常
        WebDriverWait(self.login.driver,6).until(EC.visibility_of_element_located(loc))
        # 获取报错文本信息
        msg = self.login.driver.find_element(*loc).text
        # 断言判断
        assert msg == expected

    # 测试写文章，内容为空
    def test_add_article_ContentEmpoty(self):
        title = "羡青"
        content = ""
        expected = "文章内容不能为空"

        # 进入写文章页面
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        # 填写文章标题
        self.login.driver.find_element(By.ID,'article-title').send_keys(title)
        # 切入iframe框架内
        frame1 = self.login.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(frame1)
        # 填写文章内容
        self.login.driver.find_element(By.XPATH,'/html/body').send_keys(content)
        # 切出iframe框架
        self.login.driver.switch_to.default_content()
        # 点击【发布】按钮
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        # 定位报错信息
        sleep(1)
        loc = (By.CLASS_NAME,"toast-message")
        # 等待弹框出现，6秒内未出现则抛出异常
        WebDriverWait(self.login.driver,6).until(EC.visibility_of_element_located(loc))
        # 获取报错文本信息
        msg = self.login.driver.find_element(*loc).text
        # 断言判断
        assert msg == expected

    # 测试写文章
    def test_add_article_OK(self):
        title = "羡青"
        content = "岁月拐走了单纯，人生是越走越复杂，复杂而肤浅"
        expected = "文章保存成功。"

        # 进入写文章页面
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        # 填写文章标题
        self.login.driver.find_element(By.ID,'article-title').send_keys(title)
        # 切入iframe框架内
        frame1 = self.login.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(frame1)
        # 填写文章内容
        self.login.driver.find_element(By.XPATH,'/html/body').send_keys(content)
        # 切出iframe框架
        self.login.driver.switch_to.default_content()
        # 点击【发布】按钮
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        # 定位弹框信息
        sleep(1)
        loc = (By.CLASS_NAME,"toast-message")
        # 等待弹框出现，6秒内未出现则抛出异常
        WebDriverWait(self.login.driver,6).until(EC.visibility_of_element_located(loc))
        # 获取弹框文本信息
        msg = self.login.driver.find_element(*loc).text
        # 断言判断
        assert msg == expected

        # 进入文章管理页面，查看新创建的文章
        self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)
        # 关闭浏览器
        self.login.driver.quit()