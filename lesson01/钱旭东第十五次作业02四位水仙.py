#----------------------第一 载入库-----------------------------------
#----------------------第二 数据索引---------------------------------
a=[]
#----------------------第三 子函数定义------------------------------
def si():
    for i in range(1000,10000):  #从1000到9999
        x1=i//1000                              #取千位数字
        x2=(i - x1*1000)//100                   #取百位数字
        x3=(i - x1*1000-x2*100)//10             #取十位数字
        x4=i - x1*1000 - x2*100 -x3*10          #取个位数字
        if x1**4 + x2**4 + x3**4 + x4**4 == i:
            a.append(i)
    
#-----------------------第四主程序-------------------------------

print('='*50)
print('1000到10000之间所有的水仙花数为')
si()
print(a)
