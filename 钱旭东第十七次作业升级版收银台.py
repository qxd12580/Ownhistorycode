# ------------------------------------第一   载入库----------------------------------
import time
# ------------------------------------第二   子函数定义----------------------------------
def judge():#定义判断函数
    global a
    global b
    global x
    f1=open("code.txt",'r',encoding='utf-8')
    s=f1.read()
    list=s.split(',')
    for i in range(len(list)):
        if list[i]==bn:
            a=1
            b=i
            x=i
            break
        else:
            continue
#-------------商品码库---
def file1():
    filename1=input('请输入文件名(装商品码)：')
    f1=open(filename1,'a')    #追加打开文件，直接在文件后边写
    cd=code+','
    f1.write(cd)
    f1.close()
#-------------商品名称库
def file2():
    filename2=input('请输入文件名(装商品名)：')
    f2=open(filename2,'a')    
    nm=name+','
    f2.write(nm)
    f2.close()
#-------------价格库-----
def file3():
    filename3=input('请输入文件名(装价格)：')
    f3=open(filename3,'a')    
    pi=price+','
    f3.write(pi)
    f3.close()
#-------------------------------------第四 主程序----------------------------------------
print('欢迎来到万和超市商品录入与查询系统！\n******请登录*******')
print('--------------------请输入-------------------')
m1 = input('||账号   :||',)                                       # 输入账号(2022003221)
m2 = input('||密码   :||',)                                       # 输入密码(456456)
m3 = input('||验证码 :||',)                                       # 输入验证码(CHAJ)
sum = 0
list1 = []                                                        # 用于装货物名，用于电子票据的输出
list2 = []                                                        # 用于装货价格，用于电子票据的输出
if m1 == '2022003221' and m2 == '456456' and m3 == 'CHAJ':
    print('登录成功!\n请在主菜单界面选择功能')
    k=''
    while(k==''):
        print("*************")
        print("1、录入商品信息")
        print("2、查询商品信息")
        print("3、修改商品信息")
        print("4、删除商品信息")
        print("5、    收银    ")
        print("6、退出管理系统")
        print("*************")
        num = int(input("请选择功能："))

        #录入功能
        if num == 1:
            filename=input("请输入总库文件名：")
            code=input("请扫描条码：")
            name=input("请输入商品名：")
            price=input("请输入单价：")
            f=open(filename,'a')
            fn=code+'\t'+name+'\t'+price
            fn=fn+'\n'
            f.write(fn)
            print("商品录入成功！\n")
            f.close()
            file1()
            file2()
            file3()
            k=input("要再来一次吗?(回车继续)")
        elif num==2:
            f1=open("code.txt",'r',encoding='utf-8')
            bn=input("请输入商品的码号：")
            #————————————先读商品码在切片，便于成一个简洁的
            f2=open("name.txt",'r') #装有名称的列表
            t=f2.read()             
            list1=t.split(',')
            f3=open("price.txt",'r',encoding='utf-8')
            c=f3.read()
            list2=c.split(',')
            judge()#——————进行判断
            v=list1[b]#——————将此时对应的名称装入v中
            q=list2[x]#——————将此时对应的价格装入w中,便于后面显示
            if a==1:
                print("当前商品的名称为：{}".format(v))
                print("当前商品的价格为：{}元".format(q))
            else:
                print("该商品不存在")
            k=input("要再来一次吗?(回车继续)")
        elif num==3:
            print("请输入你想替换的旧内容",end=' ')
            r1=input()
            print("请输入你想替换的新内容",end=' ')
            r2=input()
            with open('万和数据库.txt', "r+") as f:
                
                   read_data = f.read()
                   f.seek(0)
                   f.truncate()   #清空文件
                   f.write(read_data.replace(r1,r2))

            print("替换成功!")
        elif num == 4:
            f=open("万和数据库.txt","r")
            j=f.read()
            list3=j.split('\t')
            print(list3)
            flag = 0
            code = input("请输入你要下架的商品码：")
            print(list3[0])
            l=list3[0]
            if l == code:
                    #info.pop(i)#删除掉i的所有信息
                    del list3[0]#删除掉i的所有信息
                    del list3[1]
                    
                    print("删除成功！")
                    flag = 1
            else:
                print("没有找到这个商品的信息！")
            f=open("万和数据库.txt","r+")
            f.seek(0)
            f.truncate()
            k=input("要再来一次吗?(回车继续)")
        elif num == 5:
            an = ''
            while an == '':
                f1=open("code.txt",'r',encoding='utf-8')
                bn=input("请输入商品的码号：")
                f2=open("name.txt",'r') #装有名称的列表
                t=f2.read()             
                list1=t.split(',')
                f3=open("price.txt",'r')
                c=f3.read()
                list2=c.split(',')
                judge()  #判断一下
                v=list1[b]#此时的商品名称
                q=list2[x]#此时的价格
                list1.append(v)     # 用于装货物名，用于电子票据的输出
                list2.append(q)# 用于装货价格，用于电子票据的输出
                print('当前货物名为：{}'.format(v))
                print('当前货物价格为：{}'.format(q))
                sum += float(q)
                print('\n小计：{:.2f}元'.format(sum))
                an = input('继续吗？')
                print('')
            print('请付费：{:.2f}元'.format(sum))
            code = input('请出示付款码！')
            while ((len(code) != 18) or (code[0:2] not in {'10','11','12','13','14','15'})):
                code = input ('付款码有误，请出示付款码！')
            now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            print('支付成功，谢谢！\n请查看您的电子小票')
            print('________________________________________')
            print('|                                      |')
            print('|               万和超市               |')
            print('|                                      |')
            print('|单据号：036200105724                  |')
            print('|机器编号：30575470                    |')
            print('|买单时间：{}         |'.format(now))
            print('|                                      |')
            print('|商品                             金额 |')
            print('|--------------------------------------|')
            for i in range(len(list1)):
                print('|{:<5s}                      |'.format(list1[i]))
            print('|合计：{:<2}件              应收:{:>9}|'.format(len(list1)-2,sum))
            print('|--------------------------------------|')
            print('|实收金额：{:<9}                   |'.format(str(sum)))
            print('|本单折扣：0.00       舍分：0.00       |')
            print('|交易流水：3017036200102624000001      |')
            print('|中心流水：61672281295360001           |')
            print('|劵支付合计：0.00                      |')
            print('|不找零金额：0.00                      |')
            print('|                                      |')
            print('|______________________________________|')          
            k=input("要再来一次吗?(回车继续)")
            
           
        else:
            # 4 -- 退出
            print('超市商品系统已退出！')
            break  # break语句跳出循环
        
else:
    print('账号/密码/验证码输入错误！程序结束运行！')
