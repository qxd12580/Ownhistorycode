#-----------------------------------主程序-----------------------------
                                                    #六位以后得等几秒以后才能出结果
x=''
while(x==''):
    n=int(input("请输入你要计算的位数:"))
    if n==3:
        #--------------------三位---------------------------
        for i in range(100,1000):
            bai_wei,shi_wei,ge_wei = map(int,str(i))     #map映射函数,先把每个数转换为字符串,再将int()函数映射至刚刚生成的字符串序列就可以得到三个整型数字
            if bai_wei**3 + shi_wei**3 +ge_wei**3 == i:
                print('三位自幂数是:',i)
    elif n==4:
        #----------------四位------------------------
        for i in range(1000,10000):
            qian_wei,bai_wei,shi_wei,ge_wei = map(int,str(i))
            if qian_wei**4 + bai_wei**4 + shi_wei**4 +ge_wei**4 == i:
                print('四位自幂数是:',i)
    elif n==5:
        #----------五位----------------------------------------
        for i in range(10000,100000):
            wan_wei,qian_wei,bai_wei,shi_wei,ge_wei = map(int,str(i))
            if wan_wei**5 + qian_wei**5 + bai_wei**5 + shi_wei**5 +ge_wei**5 == i:
                print('五位自幂数(五角星数)是:',i)
    elif n==6:
        #------------六位---------------------
        for i in range(100000,1000000):
            shi_wan_wei,wan_wei,qian_wei,bai_wei,shi_wei,ge_wei = map(int,str(i))
            if shi_wan_wei**6 + wan_wei**6 + qian_wei**6 + bai_wei**6 + shi_wei**6 + ge_wei**6 == i:
                print('六位自幂数是:',i)
    elif n==7:
        #------------七位---------------------------
        for i in range(1000000,10000000):
            bw_wei,sw_wei,wan_wei,qian_wei,bai_wei,shi_wei,ge_wei = map(int,str(i))
            if bw_wei**7 + sw_wei**7 + wan_wei**7 + qian_wei**7 + bai_wei**7 + shi_wei**7 +ge_wei**7 == i:
                print('七位自幂数是:',i)
    else:
        #-------------八位---------------------------------
        for i in range(10000000,100000000):
            qw_wei,bw_wei,sw_wei,wan_wei,qian_wei,bai_wei,shi_wei,ge_wei = map(int,str(i))
            if qw_wei**8 + bw_wei**8 + sw_wei**8 + wan_wei**8 + qian_wei**8 + bai_wei**8 + shi_wei**8 +ge_wei**8 == i:
                print('八位自幂数是:',i)

    x=input('还想再算吗?(回车继续)')



