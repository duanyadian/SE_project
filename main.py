from util import util
from selenium import webdriver

if __name__ == '__main__':
    print(util.gen_random_str())

    driver = webdriver.Chrome()
    driver.get("http://192.166.66.25:8080/dyd/user/register")
    driver.maximize_window()
    print(util.get_code(driver,"captcha-img"))