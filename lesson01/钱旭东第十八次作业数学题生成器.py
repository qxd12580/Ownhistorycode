#----------------------第一 载入库-----------------------------
import random as rd
#----------------------第二 数据索引---------------------------
sign=['+','x','-','➗']#这里边有四个运算符
list=[x for x in range(0,100)]
jian1=[x for x in range(50,100)]
jian2=[x for x in range(0,50)]
chu1=[12,24,36,48,60,72,84,96]
chu2=[2,3,4]
#---------------------第三 子函数定义--------------------------------
#---------------------第四 主程序------------------------------------
j='y'
while(j=='y'):
    filename=input("请输入文件名：")
    grade=0
    name=input("请输入你的姓名")
    for i in range(5):#循环10次
        a1=rd.randint(0,49)#生成一个0-99的随机数
        a2=rd.randint(0,49)#生成一个0-99的随机数
        b=rd.randint(0,1)#生成一个0-3的随机数
        a3=rd.randint(0,7)
        a4=rd.randint(0,2)
        a5=rd.randint(0,49)
        a6=rd.randint(0,49)
        a7=rd.randint(0,20)
        c1=list[a7]
        c2=list[a3]
        c3=list[a1]
        c4=list[a2]
        d1=chu1[a3]
        d2=chu2[a4]
        d3=jian1[a5]
        d4=jian2[a6]
        if sign[b]=='+':
            print(list[a1],end=' ')
            print(sign[b],end=' ')
            print(list[a2],end=' ')
            print("=",end=' ')
            c=c3+c4
        if sign[b]=='-':
            print(jian1[a5],end=' ')
            print(sign[b],end=' ')
            print(jian2[a6],end=' ')
            print("=",end=' ')
            c=d3-d4
        if sign[b]=='x':
            print(list[a7],end=' ')
            print(sign[b],end=' ')
            print(list[a3],end=' ')
            print("=",end=' ')
            c=c1*c2
        if sign[b]=='➗':
            print(chu1[a3],end=' ')
            print(sign[b],end=' ')
            print(chu2[a4],end=' ')
            print("=",end=' ')
            c=d1/d2
        x=int(input())
        if x==c:
            grade+=10
            print("回答正确!")
        elif x!=c:
            print("你答错了")
            print("正确答案为%d"%c)
    for i in range(5):#循环10次
        a1=rd.randint(0,49)#生成一个0-99的随机数
        a2=rd.randint(0,49)#生成一个0-99的随机数
        b=rd.randint(2,3)#生成一个0-3的随机数
        a3=rd.randint(0,7)
        a4=rd.randint(0,2)
        a5=rd.randint(0,49)
        a6=rd.randint(0,49)
        a7=rd.randint(0,20)
        c1=list[a7]
        c2=list[a3]
        d1=chu1[a3]
        d2=chu2[a4]
        d3=jian1[a5]
        d4=jian2[a6]
        if sign[b]=='+':
            print(list[a1],end=' ')
            print(sign[b],end=' ')
            print(list[a2],end=' ')
            print("=",end=' ')
            c=c1+c2
        if sign[b]=='-':
            print(jian1[a5],end=' ')
            print(sign[b],end=' ')
            print(jian2[a6],end=' ')
            print("=",end=' ')
            c=d3-d4
        if sign[b]=='x':
            print(list[a7],end=' ')
            print(sign[b],end=' ')
            print(list[a3],end=' ')
            print("=",end=' ')
            c=c1*c2
        if sign[b]=='➗':
            print(chu1[a3],end=' ')
            print(sign[b],end=' ')
            print(chu2[a4],end=' ')
            print("=",end=' ')
            c=d1/d2
        x=int(input())
        if x==c:
            grade+=10
            print("回答正确!")
        elif x!=c:
            print("你答错了")
            print("正确答案为%d"%c)
    print("你的最终成绩为%d"%grade)
    if grade<60:
        print("不及格，要加油！")
    elif 60<=grade<90:
        print("成绩一般。")
    else:
        print("非常优秀！")
    f=open(filename,'a')
    grade1=str(grade)
    nd=name+' '+grade1
    nd=nd+'\n'
    f.write(nd)
    f.close()
    j=input("有请下一位！(y/n)")

