'''
filename=input("请输入总库文件名：")
a1=input()
a2=input()
a3=input()
a4=input()
a5=input()
a6=input()
a7=input()
a8=input()
a9=input()
a10=input()
a11=input()
a12=input()
a13=input()
a14=input()
a15=input()
a16=input()
a17=input()
a18=input()
a19=input()
a20=input()
a21=input()
a22=input()
a23=input()
a24=input()
a25=input()
a26=input()
f=open(filename,'a')
fn=a1+'\n'+a2+'\n'+a3+'\n'+a4+'\n'+a5+'\n'+a6+'\n'+a7+'\n'+a8+'\n'+a9+'\n'+a10+'\n'+a11+'\n'+a12+'\n'+a13+'\n'+a14+'\n'+a15+'\n'+a16+'\n'+a17+'\n'+a18+'\n'+a19+'\n'+a20+'\n'+a21+'\n'+a22+'\n'+a23+'\n'+a24+'\n'+a25+'\n'+a26
fn=fn+'\n'
f.write(fn)
f.close()
print("输入结束")
'''
#——————————第一 载入库——————————
import random
import turtle
import turtle as t
#——————————第二 数据索引————————————
ls = [turtle.Turtle() for i in range(30)]
ls2 = []#高度
ls3 = []#速度
ls4 = []#内容
ls5 = []#内容
ls6 = []#字体大小
ls7 = ['red','black','green','yellow','lime','blue']#字体颜色
t.tracer(100)
#——————————第三 子函数定义——————————
def rd():#读文件
    f=open("弹幕库.txt", "r")
    for line in f:
        ls = line.strip()
        ls4.append(ls)
    f.close()
    return ls4

def move():#设置初始
    t.tracer(100)
    for i in range(30):
        ls[i].penup()
        a = random.randint(-200,200)#高度
        ls[i].goto(400,a)
        ls[i].hideturtle()
        b = random.randint(1,10)#速度
        ls2.append(b)
        c = random.randint(1,20)#距离
        ls3.append(c)
        d = random.randint(0,11)#内容
        ls5.append(ls4[d])
        e = random.randint(10,30)#字体大小
        ls6.append(e)
        d = random.randint(0,5)
        ls[i].color(ls7[d])
    t.update()
    return ls2,ls3,ls5,ls6
#——————————第四  主程序——————————
rd()
print(ls4)
move()
while True:
    for i in range(30):
        ls[i].pendown()
        ls[i].setheading(-180)
        ls[i].clear()
        ls[i].speed(ls2[i])
        ls[i].forward(ls3[i])
        ls[i].write(ls5[i],align="center",font=('',ls6[i],''))
    for i in range(30):
        if ls[i].xcor()<=-400:
            ls[i].setheading(-180)
            ls[i].clear()
            ls[i].penup()
            a = random.randint(-200, 200)
            ls[i].goto(400,a)
            ls[i].write(ls5[i],align="center",font=('',ls6[i],''))
