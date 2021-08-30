from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait # 显性等待

class TestGoods(object):
    def __init__(self,login):
        self.login = login

    # 测试添加商品，商品标题为空
    def test_add_GoodnameEmpty(self):
        describe = "这里是商品描述"
        price = 1999
        expected = "产品标题不能为空"
        # 点击商品，展开商品菜单
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[6]/a/span[1]').click()
        # 点击商品列表，进入商品列表页面
        sleep(1)
        self.login.driver.find_element(By.XPATH,"//*[@id='sidebar-menu']/li[6]/ul/li[1]/a").click()
        # 点击【新建】
        self.login.driver.find_element(By.XPATH,'/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a').click()
        # 切入frame框架内
        sleep(1)
        iframe = self.login.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(iframe)
        # 输入商品描述
        sleep(1)
        self.login.driver.find_element(By.XPATH,'/html/body').send_keys(describe)
        # 切出frame框架
        self.login.driver.switch_to.default_content()
        # 输入商品价格
        self.login.driver.find_element(By.ID,"price").send_keys(price)
        # 选择分类，(前置条件是已存在商品分类)
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[2]/div[2]/div/div[2]/label/input').click()
        # # 添加商品图片，(前置条件是相册图库存在图片)
        # sleep(1)
        # self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[4]/div[3]/button').click()
        # # 选择图片
        # elem = self.login.driver.find_element(By.XPATH,'//*[@id="activity"]/div[1]')
        # print(elem)
        # elem[2].click()
        # 点击【上架】
        sleep(1)
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        # 定位提示信息
        sleep(1)
        loc = (By.CLASS_NAME,"toast-message")
        # 等待提示信息出现
        WebDriverWait(self.login.driver,3).until(EC.visibility_of_element_located(loc))
        # 获取提示文本信息
        msg = self.login.driver.find_element(*loc).text
        # 断言
        assert msg == expected

    # 测试添加商品，商品价格为空
    def test_add_GoodpriceEmpty(self):
        title = "某手机"
        describe = "这里是商品描述。"
        price = ""
        expected = "产品的销售价格不能为空"
        # # 点击商品列表，进入商品列表页面
        # self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[6]/ul/li[1]/a').click()
        # # 点击【新建】
        # self.login.driver.find_element(By.XPATH,'/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a').click()
        # 清空名称后重新输入商品名称
        self.login.driver.find_element(By.ID,"product-title").clear()
        self.login.driver.find_element(By.ID,"product-title").send_keys(title)
        # 切入frame框架内
        iframe = self.login.driver.find_element(By.XPATH,'//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(iframe)
        # 情况描述后重新输入
        sleep(1)
        self.login.driver.find_element(By.XPATH,'/html/body').clear()
        self.login.driver.find_element(By.XPATH,'/html/body').send_keys(describe)
        # 切出frame框架
        self.login.driver.switch_to.default_content()
        # 清空商品价格
        self.login.driver.find_element(By.ID, "price").clear()
        # 选择分类，(前置条件是已存在商品分类)
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[2]/div[2]/div/div[2]/label/input').click()
        # 点击【上架】
        self.login.driver.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        # 定位提示信息
        sleep(1)
        loc = (By.CLASS_NAME,"toast-message")
        # 等待提示信息出现
        WebDriverWait(self.login.driver,3).until(EC.visibility_of_element_located(loc))
        # 获取提示文本信息
        msg = self.login.driver.find_element(*loc).text
        # 断言
        assert msg == expected

    # 测试添加商品成功
    def test_add_Good_OK(self):
        title = "手机"
        describe = "这里是商品描述！！！"
        price = "1888"
        expected = "产品保存成功。"
        # # 点击商品列表，进入商品列表页面
        # self.login.driver.find_element(By.XPATH, '//*[@id="sidebar-menu"]/li[6]/ul/li[1]/a').click()
        # # 点击【新建】
        # self.login.driver.find_element(By.XPATH,
        #                                '/html/body/div/div/section[3]/div/div/div/div[1]/div/div/a').click()
        # 清空名称后重新输入商品名称
        self.login.driver.find_element(By.ID, "product-title").clear()
        self.login.driver.find_element(By.ID, "product-title").send_keys(title)
        # 切入frame框架内
        iframe = self.login.driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/iframe')
        self.login.driver.switch_to.frame(iframe)
        # 清空商品描述后重新输入
        sleep(1)
        self.login.driver.find_element(By.XPATH, '/html/body').clear()
        self.login.driver.find_element(By.XPATH, '/html/body').send_keys(describe)
        # 切出frame框架
        self.login.driver.switch_to.default_content()
        # 清空价格后重新输入商品价格
        self.login.driver.find_element(By.ID, "price").clear()
        self.login.driver.find_element(By.ID, "price").send_keys(price)
        # 选择分类，(前置条件是已存在商品分类)
        self.login.driver.find_element(By.XPATH,
                                       '//*[@id="form"]/div/div[2]/div[2]/div[2]/div/div[2]/label/input').click()
        # 点击【上架】
        self.login.driver.find_element(By.XPATH, '//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()
        # 定位提示信息
        sleep(1)
        loc = (By.CLASS_NAME, "toast-message")
        # 等待提示信息出现
        WebDriverWait(self.login.driver, 3).until(EC.visibility_of_element_located(loc))
        # 获取提示文本信息
        msg = self.login.driver.find_element(*loc).text
        # 断言
        assert msg == expected
        # 查看商品列表
        self.login.driver.find_element(By.XPATH,'//*[@id="sidebar-menu"]/li[6]/ul/li[1]/a').click()
        sleep(1)

        # 关闭浏览器
        self.login.driver.quit()
