import allure
import pytest
from selenium import webdriver

# 使用钩子函数实现识别用例失败，然后实现截图并添加到allure，
# 同时针对driver做了自定义的fixture，全局性的driver，用例一执行就创建这个driver
# 然后通过fixture传到用例中

driver = None # 自定义一个driver=None
@pytest.hookimpl(tryfirst=1,hookwrapper=1)
def pytest_runtest_makereport(item,call):   # 钩子函数
    # 用例执行完成后再执行此操作，（后置处理用yield）
    outcome = yield # yield表示测试用例执行完了，接下来要做什么事情
    rep = outcome.get_result() # 获取用例执行完成之后的结果
    if rep.when == "call" and rep.failed:   # 若结果正在被调用而且是失败的则进行截图
        # 截图方法需要用到driver对象
        img = driver.get_screenshot_as_png()  # 若出现异常，则进行截图操作
        allure.attach(img, "失败截图", allure.attachment_type.PNG)  # 将图片展现在Allure报告上

# 自定义一个Fixture，初始化driver对象
@pytest.fixture(scope="session",autouse=True)
def init_driver():
    global driver
    driver = webdriver.Chrome()
    return driver  # 返回初始化后的driver，就可以直接被调用啦
