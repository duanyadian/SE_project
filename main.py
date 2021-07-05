from testcases.First_round_test.test_user_register import TestUserRegister
from testcases.First_round_test.test_user_login import TestUserLogin
from testcases.First_round_test.test_admin_login import TestAdminLogin
from testcases.First_round_test.test_category import TestCategory
from  testcases.First_round_test.test_article import TestArticle
from  testcases.First_round_test.test_article_delete import TestArticleDel
from testcases.Second_round_test.test_goods import TestGoods

if __name__ == '__main__':
    # # 执行test_user_register用例
    # case = TestUserRegister()
    # case.test_user_register_username()
    # case.test_user_register_email()
    # case.test_user_register_pwd()
    # case.test_user_register_Confirmpwd()
    # case.test_user_register_different()
    # case.test_register_code_error()
    # case.test_user_register_OK()
    #
    # # 执行test_user_login用例
    # case1 = TestUserLogin()
    # case1.test_user_login_nameEmpty()
    # case1.test_user_login_nameError()
    # case1.test_user_login_pwdEmpty()
    # case1.test_user_login_pwdError()
    # case1.test_user_login_OK()

    # 执行test_admin_login用例
    case2 = TestAdminLogin()
    # case2.test_admin_login_nameEmpty()
    # case2.test_admin_login_nameError()
    # case2.test_admin_login_pwdEmpty()
    # case2.test_admin_login_pwdError()
    # case2.test_admin_login_captchaEmpty()
    # case2.test_admin_login_captchaError()
    case2.test_admin_login_OK()

    # # 执行test_catepory用例，需先登录后台
    # case3 = TestCategory(case2) # 调用登录
    # case3.test_add_CategoryEmpoty()
    # case3.test_add_SulgEmpoty()
    # case3.test_add_OK()

    # # 执行test_article用例，需先登录后台
    # case4 = TestArticle(case2)
    # case4.test_add_article_TitleEmpoty()
    # case4.test_add_article_ContentEmpoty()
    # case4.test_add_article_OK()

    # # 执行test_article_delete用例，需先登录后台,存在多篇文章
    # case5 = TestArticleDel(case2) # 调用登录
    # case5.test_del_one_article()
    # case5.test_del_all_article()

    # 执行test_goods用例，需先登录
    case6 = TestGoods(case2)
    case6.test_add_GoodnameEmpty()
    case6.test_add_GoodpriceEmpty()
    case6.test_add_Good_OK()