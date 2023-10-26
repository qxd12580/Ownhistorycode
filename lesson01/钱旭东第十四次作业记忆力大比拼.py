#-----------------------------第一部分 载入库

from turtle import*#方便
import random as r
import time
#-----------------------------第二部分  数据驱动----------------------------
#-------------------------------第三部分 定义子函数--------------------
def move(x,y):#方便
    seth(90)
    pu()
    goto(x,y)
    pd()

def pm(x,y):#编辑牌框程序
    move(x,y)
    hideturtle()
    tracer(0)#快速画完
    fd(55)
    circle(-5,90)
    fd(60)
    circle(-5,90)
    fd(130)
    circle(-5,90)
    fd(60)
    circle(-5,90)
    fd(80)
    a=r.randint(0,54)#随机选择
    move(x,y+20)
    write(p[a][0],font=(60))#寻花色与数字
    move(x,y+40)
    write(p[a][1],font=60)
    move(x+10,y-40)
    write(p[a][0],font=('宋体',50))#加字体，才能调大字体
    move(x+60,y-80)
    write(p[a][1],font=60)
    move(x+60,y-60)
    write(p[a][0],font=200)
    tracer(1)

#------------------------------第四部分 主程序----------------------------
    #运行poke
p=[]
hs=["♥","♦","♠","♣"]
q=[]
wang=['大王','小王']

for i in range(4):              #循环四次，取红心，方块，黑桃，梅花
    for a in range(13):         #循环十七次，a取值从0到13
        if (a==0):              #改变10到12数字
            b="A"
        elif (a==10):
            b="J"
        elif (a==11):
            b="Q"
        elif (a==12):
            b="K"
        else:
            b=str(a+1)
        q.append(b)

for i in range(4):       #花色数字分开，方便最后画图
     for a in range(13):
        c=[hs[i],q[a]]
        p.append(c)
p.append(wang[0])#加入大小王
p.append(wang[1])
print(p)



screensize(bg='pink') #设置背景颜色   
while(True):#死循环
    write('你有2s秒记忆',font=('黑体',30))#设置提示
    pm(-300,-100)
    pm(-200,-100)
    pm(-100,-100)
    time.sleep(2)
    move(-200,0)    
    clear()#删字
    write('你有10s秒回忆',font=('黑体',30))    
    time.sleep(10)
    clear()
