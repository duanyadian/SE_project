# 导入库
import os
import pickle
import random
import string
import time
from PIL import Image
from lib.ShowapiRequest import ShowapiRequest

def get_code(driver, id):
    # 获取验证码图片
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + "\\screenshots"
    picture_name = path + "\\" + str(t) + ".png"

    driver.save_screenshot(picture_name)

    ce = driver.find_element_by_id(id)

    left = ce.location["x"]
    top = ce.location["y"]
    right = ce.size["width"] + left
    height = ce.size["height"] + top

    im = Image.open(picture_name)
    img = im.crop((left,top,right,height))

    t = time.time()

    picture_name1 = path + "\\" + str(t) + ".png"
    img.save(picture_name1) # 这就是截取到的验证码图片

    r = ShowapiRequest("http://route.showapi.com/184-4", "685820", "2efb2dd481404309b5f624151d93bdc6")
    r.addFilePara("image", picture_name1)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()["showapi_res_body"]
    result = text["Result"] # 识别到的验证码结果
    return result

# 生成随机字符串,字母加数字组合
def gen_random_str():
    rand_str = "".join(random.sample(string.ascii_letters + string.digits, 6))
    return rand_str

# 保存Cookie
def save_cookie(driver,path):
    with open(path, "wb") as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies,filehandler)

# 加载Cookie
def load_cookie(driver,path):
    with open(path,"rb") as cookiefile:
        cookies = pickle.load(cookiefile)
        for cookie in cookies:
            driver.add_cookie(cookie)