import pytest
@pytest.fixture()				# 默认范围为函数级(function)
def login():
    print("请先登录")
    return
def test_Search():				# 不需要登录，所以不调用fixture
    print("搜索商品，无需登录")
def test_Cart(login):			# 需要登录，调用fixture
    print("加购商品，需登录")

@pytest.fixture(scope="class")	# 设置范围为类级(class)
def login():
    print("请登录后再购买")
    return
class Testfix(object):
    def test_Look(self):
        print("查看商品，无需登录")	# 不需要登录，所以不调用fixture
    def test_Pay(self,login):
        print("购买商品，需登录")	# 需要登录，调用fixture