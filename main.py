from testcases.First_round_test.test_user_register import TestUserRegister
from testcases.First_round_test.test_user_login import TestUserLogin

if __name__ == '__main__':
    case = TestUserRegister()
    case.test_user_register_username()
    case.test_user_register_email()
    case.test_user_register_pwd()
    case.test_user_register_Confirmpwd()
    case.test_user_register_different()
    case.test_register_code_error()

    case1 = TestUserLogin()
    case1.test_user_login_nameEmpty()
    case1.test_user_login_nameError()
    case1.test_user_login_pwdEmpty()
    case1.test_user_login_pwdError()
    case1.test_user_login_OK()