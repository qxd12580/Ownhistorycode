#商品信息管理系统
#实现功能：录入，查询，退出系统
print("欢迎使用商品管理系统")

infos = {}#用来装商品信息，创建一个列表

while True:
    print("*************")
    print("1、录入商品信息")
    print("2、查询商品信息")
    print("3、退出管理系统")
    print("*************")
    num = int(input("请选择功能："))

    #录入功能
    if num == 1:
        code=input("请扫描条码")
        name=input("请输入商品名")
        price=float(input("请输入单价"))
        infos[code]=[name,price]
        print("商品录入成功！\n")

    #查找功能
    elif num == 2:
        
        code=input("请扫描条码")
        print("商品名称为{}".format(infos[code][0]))
        print("商品单价为{}".format(infos[code][1]))
    



    elif num == 3:
        print("成功退出系统！")
        break
