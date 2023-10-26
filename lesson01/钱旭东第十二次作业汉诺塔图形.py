#-----------------------第一部分 载入库--------------------------------
import turtle as t
#----------------------第三部分定义子函数----------------------------------
#--------画柱子-----
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def zhu(x,y):
    for i in range(3):
        t.setheading(0)
        go(x+250*i,y)
        t.forward(100)
        go(x+50+250*i,y)
        t.setheading(90)
        t.forward(300)


#-------定义箭头-------    
def jiantou(n):
    panzi=[t.Turtle()for i in range(n)]
    for i in range(n):
        panzi[i].penup()
        panzi[i].hideturtle()
        panzi[i].shape('square')
        panzi[i].shapesize(1,8-i)
        panzi[i].goto(-250,-190+20*i)
        panzi[i].showturtle()
    return panzi
def move(n,a,b,c):
    panzi[m-n].goto(a[0],200)
    panzi[m-n].goto(c[0],200)
    panzi[m-n].goto(c[0],-190+c[1]*20)
    a[1]+=-1
    c[1]+=1
def ta(n,a,b,c):       #文字版转换
    if n==1:
        move(n,a,b,c)
    else:
        ta(n-1,a,c,b)
        move(n,a,b,c)
        ta(n-1,b,a,c)



#-----------------------第四部分主程序--------
t.speed(0)
t.hideturtle()
t.pensize(5)
zhu(-300,-200)
n=int(input('请输入汉诺塔的层数:'))
m=n
panzi=jiantou(n)
a=[-250,n]
b=[0,0]
c=[250,0]
ta(n,a,b,c)
input()
    
