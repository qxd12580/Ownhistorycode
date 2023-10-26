import turtle as t
import time
 
def star(a,len,x,y):

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(a)

    t.color("yellow","yellow")
    t.begin_fill()

    for i in range(5):
        t.right(144)
        t.forward(len)
    t.end_fill()

    t.hideturtle()

def flag(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.color("red","red")
    t.begin_fill()

    t.forward(350)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(200)
    t.end_fill()

    t.hideturtle()
def china(x,y):
    t.tracer(0)   #关闭轨迹
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.speed(0)
    flag(x,y)
    star(0,60,100+x,-50+y)
    star(0,20,120+x,-20+y)
    star(0,20,140+x,-50+y)
    star(0,20,140+x,-70+y)
    star(0,20,100+x,-50+y)
    t.tracer(1)


for i in range(1000):
    china(0,-100+i*5)
    t.sleep(0.05)
    t.clear()
































