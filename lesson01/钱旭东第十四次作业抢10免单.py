#------------------------------第一 载入库---------------------
import turtle,time


#-----------------------------第三 子函数定义-----------------------------
#------------增加点击屏幕暂停的功能-------------------
def p(x,y):  #一旦屏幕点击，本程序就运行一次
    global k
    k=1
#-----------------显示标题-----------------
def heading():
    t1.hideturtle()
    t1.pencolor('red')
    t1.penup()
    t1.goto(-290,100)
    t1.pendown()
    
    t1.write("抢十免单",font=('楷体',60))
#-----------------显示数值------------------
def number():
    d=float(0)
    t2.hideturtle()
    t2.penup()
    for i in range(1200):
        d+=0.01         #1帧为0.10s
        t2.goto(-170,-50)
        t2.write("{:.2f}".format(d),font=("宋体",150))     #写数字
        if k==1:            #如果k值为1，则点击了屏幕启动了p子函数，休息100秒
            time.sleep(100)
        time.sleep(0.01)     #数字间隔为0.01s
        t2.clear()     #数字显示后清除
        t2.hideturtle()    
            
    
#----------------------------------第四 主程序---------------------------
t1=turtle.Pen()#定义俩画笔
t2=turtle.Pen()
heading()
k=0
turtle.onscreenclick(p)
number()
