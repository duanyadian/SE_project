from time import sleep

from selenium import webdriver

class TestCookie(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_loginBcookie(self):
        self.driver.get("https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window")
        cks = self.driver.get_cookies() # 获取所有Cookie
        for ck in cks:
            print(ck) # 打印每条Cookie
        print("*****************************************************")

    def test_loginAcookie(self):
        self.driver.get("https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window")
        sleep(60)
        cks = self.driver.get_cookies() # 获取所有Cookie
        for ck in cks:
            print(ck) # 打印每条Cookie
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window")
        sleep(1)
        self.driver.add_cookie({'name': 'DedeUserID','value': '99118103'}) # 新增cookie
        sleep(1)
        self.driver.get("https://space.bilibili.com/99118103/favlist") # 访问个人收藏页面

if __name__ == '__main__':
    case = TestCookie()
    # case.test_loginBcookie()
    # case.test_loginAcookie()
    case.test_cookie()