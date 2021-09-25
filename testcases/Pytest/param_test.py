
import pytest
import allure

list = [1,"1+1","1+2"] # 列表
# ↓参数必须与值的个数相等，可以使用ids参数重命名，值可自定义只要方便理解其意思即可
@pytest.mark.parametrize("value",list,ids=["value=1","value=2","value=3"])
def test_list(value):
    print(value)

tuple = [("abc"),("def"),["g","h","i"],[1,2,3]] # 元组
@pytest.mark.parametrize("x,y,z",tuple)  # 参数必须与值的个数相等
def test_xzy(x,y,z):
    print(x,y,z)

@pytest.mark.parametrize("user,pwd,vcode",[("dyd","123456","666"),("duan","654321","666")]) # 直接传递多参数
def test_param(user,pwd,vcode):
    print(user,pwd,vcode)

dict = ({"username":"dyd","passwd":123456},{"phone":18888888888,"age":18}) # 字典
@pytest.mark.parametrize("dic",dict)
def test_dict(dic):
    print(dic)

data = [ # ↓通过pytest中的param定义参数，id是对参数的一个说明，可自定义，方便理解各用例的含义即可
    pytest.param(100,100,200,id="a+b:pass"),
    pytest.param("a","b","ab",id="a+b:pass"),
    pytest.param(1,1,6,id="a+b:fail")]
def add(a,b): # 定义一个add相加的函数
    return a+b
class TestParam(object):
    @pytest.mark.parametrize("a,b,expect",data)
    def test_param(self,a,b,expect):
        assert add(a,b) == expect # 调用a+b，判断实际结果是否与期望结果一致

@pytest.mark.parametrize("input,expect",[("1+1",2),("2+2",4)])
def test_count(input,expect):
    assert eval(input) ==expect # 估算实际结果是否与期望结果一致

@pytest.mark.parametrize("x",(1,2,3))
@pytest.mark.parametrize("y",(4,5,6))
def test_dkej(x,y):
    print(f"打印组合方式：({x},{y})") # 通过参数化实现笛卡尔积


# * 模块级 setup_module/teardowm_module             开始于模块始末，全局的
# * 类级     setup_class/teardown_class             只在类中前后运行一次（在类中）
# * 函数级 setup_function/teardown_function         只对函数用例生效（在类外）
# * 方法级 setup_method/teardown_method             类中的每个方法执行前后（在类中）
# * 类中的 setup/teardown                           运行在调用方法前后（常用）


def setup_module():
    print("setup_模块级")
def teardown_module():
    print("teardown_模块级")
def setup_function():
    print("setup_函数")
def teardown_function():
    print("teardown_函数")

def test_01():
    print("测试01")

def test_02():
    print("测试02")
@allure.severity()
class Testcase01(object):
    @classmethod
    def setup_class(cls):
        print("setup_类")
    def teardown_class(cls):
        print("teardown_类")
    def setup_method(cls):
        print("setup_方法")
    def teardown_method(cls):
        print("teardown_方法")
    def setup(cls):
        print("setup")
    def teardown(cls):
        print("teardown")

    def test_03(self):
        print("测试03")
    def test_04(self):
        print("测试04")