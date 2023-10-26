a=''
while(a==''):


    x=float(input('你想选择公式法一算圆周率(1)，还是公式法2算圆周率(2),或蒙特利落法算(3)'))

    if x==2:

        a=0
        b=1
        while (1/((b*2)-1)) >1e-6:
            a+=((-1)**(b-1))/((2*b)-1)
            b+=1
        pi=a*4

        print("圆周率：{:.10f}".format(pi))

    elif x==1:
        pi=0
        for i in range(100):
            pi+=1/pow(16,i)*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
        print('{:.11}'.format(pi))    

    else:
        from math import sqrt
        from random import random

        def cal_PI(N):
            hits=0
            for i in range(1,N*N+1):
                x,y=random(),random()
                if sqrt(x**2+y**2)<=1:
                    hits+=1
                else:
                    hits=hits
                PI=(hits*4)/(N**2)    
            return PI
        print('{:.11}'.format(cal_PI(1000)))

    a=input('还想再玩一次吗?(输入回车继续)')

