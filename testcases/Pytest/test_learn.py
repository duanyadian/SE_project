# 文件名称命名规则，以test_或_test结尾
import pytest

def test_func():  # 在类外面称为函数，函数命名规则，以test_开头
    assert 1 == 1

class Testpy(object):  # 类命名规则，以Test开头
    def test_method(self):  # 在类中称为方法，方法命名规则与函数一样，以test_开头
        assert 1 + 2 == 3

    @pytest.mark.smoke
    def test_func1(self):
        print("这是练习！")
@pytest.mark.output
class caseCls(object):
    def dyd_case(self):
        print("修改函数后的规则验证")


if __name__ == '__main__':
    pytest.main(["test_learn.py"])  # 通过main函数执行命令

# 通过命令执行用例
# pytest ../Pytest                              执行包中所有模块的用例
# pytest -vs test_learn.py                      执行单独的pytest模块，test_learn.py文件
# pytest -vs test_learn.py::Testpy              只执行文件中的Testpy类
# pytest -vs test_learn.py::Testpy::test_method 只执行文件中Testpy类下的test_math方法
# pytest -vs test_learn.py::test_function       只执行文件中test_func函数

