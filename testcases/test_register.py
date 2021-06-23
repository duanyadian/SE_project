# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # 打开浏览器
# driver = webdriver.Chrome()
# # 打开网页
# driver.get("http://192.166.66.25:8080/dyd/user/register")
# # 定位元素
# driver.find_element(By.NAME,"username").clear()
# username = driver.find_element(By.NAME,"username").send_keys("dyd")

# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","683598","457cebc139e74f25b5ab0eb7c53a7a24" )
r.addFilePara("image", "../screenshots/123.png")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
result = res.text
print(result)
res_body = res.json()["showapi_res_body"]
print(res_body)
print(res_body["Result"]) # 返回信息