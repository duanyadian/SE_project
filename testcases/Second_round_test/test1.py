name = input("请输入姓名：")
college = input("请输入毕业院校：")
year = int(input("请输入年份："))
month = int(input("请输入月份："))
print(f"我叫{name}，毕业于{college}，毕业时间是{year}年{month}月")
print(f"我叫%s，毕业于%s，毕业时间是%d年%d月"%(name,college,year,month))