import requests

class Testreq(object):
    def test_req(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.json())      # 获取并打印json解码后的内容
        print(r.status_code) # 获取并打印现在该请求的状态码
        print(r.text)        # 获取并打印获取的文本内容
        print(r.headers)     # 获取并打印响应头信息
        print(r.request.headers) # 获取并打印请求头信息
        print(r.url)         # 获取并打印编码后请求的url
        assert r.json()["url"] == "https://httpbin.testing-studio.com/get" # 断言判断返回结果中url是否正确

    def test_pj(self):
        url = "https://httpbin.testing-studio.com/"
        # 定制请求方法一
        param = {"name":"dyd","class":"csb"}
        a = requests.get(url+"get",params=param)
        print(a.json())
        assert a.json()["url"] == "https://httpbin.testing-studio.com/get?name=dyd&class=csb"

        header = {'Host': 'httpbin.testing-studio.com','Accept-Encoding': 'Content'}
        b = requests.request("post",url+"post",headers= header)
        print("定制请求的第二种方法",b.json())
        assert b.json()["url"] == "https://httpbin.testing-studio.com/post"

        c = requests.request("patch",url+"patch")
        print(c.json())
        assert c.json()["url"] == "https://httpbin.testing-studio.com/patch"

    def test_delete(self):
        url = "https://httpbin.testing-studio.com/"
        d = requests.request("delete",url+"delete")
        print(d.json())
        assert d.json()["url"] == "https://httpbin.testing-studio.com/delete"


