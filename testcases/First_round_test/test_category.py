from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCategory(object):
    def __init__(self, login):
        self.login = login

    # 测试文章分类名称为空
    def test_add_CategoryEmpoty(self):
        title = ""
        parent = "顶级"
        slug = "www.dyd.com"
        content = "这是正文内容"
        describe = "这是文章描述"
        expected = "分类名称不能为空"

        # 点击文章，展开文章菜单
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        # 点击分类，进入分类页面
        sleep(1)
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

        # 输入分类名称
        self.login.driver.find_element(By.NAME,"category.title").send_keys(title)
        # 选择父分类
        parent_catepory_elem = self.login.driver.find_element(By.NAME,"category.pid")
        # 选择下拉列表中的分类，使用Select的class，使用可视化文本
        Select(parent_catepory_elem).select_by_visible_text(parent)
        # 输入slug
        self.login.driver.find_element(By.NAME,"category.slug").send_keys(slug)
        # 输入内容
        self.login.driver.find_element(By.NAME,"category.content").send_keys(content)
        # 输入描述
        self.login.driver.find_element(By.NAME,"category.meta_description").send_keys(describe)
        # 点击【提交】按钮
        sleep(1)
        self.login.driver.find_element(By.XPATH,
                                       '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()
        # 定位报错信息
        sleep(1)
        loc = (By.CLASS_NAME,"toast-message")
        # 等待报错信息出现，限时5秒，5秒内未出现则抛出异常
        WebDriverWait(self.login.driver,5).until(EC.visibility_of_element_located(loc))
        # 获取报错文本信息
        msg = self.login.driver.find_element(*loc).text

        # 通过断言验证报错信息是否正确
        assert msg == expected

        # 测试文章分类slug为空
        def test_add_CategoryEmpoty(self):
            title = "这是标题"
            parent = "顶级"
            slug = ""
            content = "好好学习，天天向上"
            describe = "这是文章描述"
            expected = "slug 不能为空"

            # 点击分类，重新加载分类页面
            sleep(1)
            self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()

            # 输入分类名称
            self.login.driver.find_element(By.NAME, "category.title").send_keys(title)
            # 选择父分类
            parent_catepory_elem = self.login.driver.find_element(By.NAME, "category.pid")
            # 选择下拉列表中的分类，使用Select的class，使用可视化文本
            Select(parent_catepory_elem).select_by_visible_text(parent)
            # 输入slug
            self.login.driver.find_element(By.NAME, "category.slug").send_keys(slug)
            # 输入内容
            self.login.driver.find_element(By.NAME, "category.content").send_keys(content)
            # 输入描述
            self.login.driver.find_element(By.NAME, "category.meta_description").send_keys(describe)
            # 点击【提交】按钮
            sleep(1)
            self.login.driver.find_element(By.XPATH,
                                           '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()
            # 定位报错信息
            sleep(1)
            loc = (By.CLASS_NAME, "toast-message")
            # 等待报错信息出现，限时5秒，5秒内未出现则抛出异常
            WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))
            # 获取报错文本信息
            msg = self.login.driver.find_element(*loc).text

            # 通过断言验证报错信息是否正确
            assert msg == expected
