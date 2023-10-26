#--------------------------第一 载入数据库-------------------------
import turtle as t
import time
#--------------------------第二 数据索引----------------------------
ls1=[[-200,-300]]
ls2=[[0,-200]]
ls4=[[60,-60]]
#——----------------------第三 子函数定义-------------------------
#定义第一个图
def di1():
    t1=t.Pen()#黑色进度条
    t2=t.Pen()#显示的百分数
    t1.pensize(50)#笔的粗细
    t1.penup()
    t1.goto(ls1[0])
    t1.pendown()
    t1.color("pink")
    a=0
    for i in range(400):
        #进度条
        t.tracer(0)
        t1.speed(0)
        t1.goto(-200+i*1,-300)
        #百分数
        t2.clear()
        a+=0.25
        t2.hideturtle()
        t2.penup()
        t2.goto(ls2[0])
        t2.pendown()      
        t2.write("{:.1f}%".format(a),font=('楷体',45))
        t.tracer(1)
        time.sleep(0.01)
#定义第二个图       
def di2():
    a=0
    t3=t.Pen()  #-------------定义画笔-
    t4=t.Pen()
    t3.hideturtle()
    t4.hideturtle()
    for i in range(500):
        t.tracer(0)
        t3.penup()
        t3.pensize(25)
        t3.pendown()
        t3.color("blue")
        t3.circle(100,0.7)
        t4.penup()
        t4.clear()
        a+=0.2
        t4.goto(ls4[0])
        t4.pendown()
        t4.write('{:.1f}%'.format(a),font=('宋体',45))
        time.sleep(0.01)
        t.tracer(1)
#-------------------------第四 主程序--------------------        
di1()
di2()

    
    
