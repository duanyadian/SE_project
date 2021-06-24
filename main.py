from testcases.First_round_test.test_user_login import TestUserLogin
from testcases.First_round_test.test_user_register import TestUserRegister
from util import util
from selenium import webdriver

if __name__ == '__main__':
    # print(util.gen_random_str())

    # driver = webdriver.Chrome()
    # driver.get("http://192.166.66.25:8080/dyd/user/register")
    # driver.maximize_window()
    # print(util.get_code(driver,"captcha-img"))

    # case = TestUserRegister()
    # case.test_register_code_error()
    case1 = TestUserLogin()
    case1.test_user_login_code_error()
    case1.test_user_login_OK()