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
    # 把截图放到screenshots目录下
    path = os.path.dirname(os.path.dirname(__file__)) + "\\screenshots"
    # 以当前时间戳命名
    picture_name = path + "\\" + str(t) + ".png"
    # 保存截图
    driver.save_screenshot(picture_name)
    # 根据验证码id获取验证码位置
    ce = driver.find_element_by_id(id)

    # 定位左顶点坐标,即左和上边界，需要确认下电脑显示的缩放比，默认100%，若不同需乘以缩放比
    left = ce.location["x"]*1.5
    top = ce.location["y"]*1.5
    # 定位右底点坐标，即右和下边界
    right = (ce.size["width"] + left)*1.5
    bottom = (ce.size["height"] + top)*1.5
    # 将值放到元组中(顺序：左上右下)
    local = (left,top,right,bottom)
    # 打开图片
    i = Image.open(picture_name)
    # 抠图
    img = i.crop(local)
    img = img.convert("RGB")

    t = time.time()
    # 根据时间戳保存为另一张图片
    picture_name1 = path + "\\" + str(t) + ".png"
    img.save(picture_name1) # 这就是截取到的验证码图片

    r = ShowapiRequest("http://route.showapi.com/184-4", "691844", "0de9ca8d0b704975a9afd9caea7b3abb")
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