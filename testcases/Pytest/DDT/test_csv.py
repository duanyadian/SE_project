import csv
import pytest

def get_data():

    with open("my_data.csv","r",encoding='UTF-8') as j:    # 只读模式打开csv文件
        data = csv.reader(j)    # csv.reader(f)返回一个csv_reader对象
        lst = []
        for row in data: # 遍历对象，每次返回一行
            lst.extend(row)   # 将数据一次性追加到lst中，将结果写到一个列表中
        return lst  # 返回lst

@pytest.mark.parametrize("csv_value",get_data())    # 调用csv数据
def test_read(csv_value):
    print(csv_value)    # 将写在列表中的数据一个一个的输出