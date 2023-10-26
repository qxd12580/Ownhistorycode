x=''
while(x==''):

    n=int(input("请输入你要求前几项的和"))
    def num(n):
        if n==1:
            return 1
        elif n==2:
            return 1
        else:
            return num(n-1)+num(n-2)
    a=num(n)
    print(a)
    x=input('还想再玩一次吗(输入回车继续)')
