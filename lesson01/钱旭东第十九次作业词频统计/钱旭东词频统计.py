#--------第一 载入库------
import jieba
from pyecharts.charts import Bar
#--------第二 数据---------
#-----2021
mk={}#创建一个字典
with open('政府工作报告2021.txt','r',encoding='utf-8') as f:#打开文件把内容给到f然后关闭
    zf1 = f.readlines()    #得到文件内容列表
jy={} #装教育
m={}
#-----2022
mk1={}#创建一个字典
with open('政府工作报告2022.txt','r',encoding='utf-8') as f:#打开文件把内容给到f然后关闭
    zf2 = f.readlines()    #得到文件内容列表
au={} #装教育
k={}
#------- 第四 主程序---------
#-------------2021--------------
for z1 in zf1:
    k1=jieba.lcut(z1, cut_all = True)   #全模式切分，
    for c1 in k1:
        if len(c1)==2:
            mk[c1] = mk.get(c1,0) + 1   #获取键值对,有这项加一 没这项给值填0                               
        if c1.count("教育")!=0:
            jy[c1] = jy.get(c1,0) + 1

mp = list(mk.items())#item函数 以列表形式返回可遍历的（键,值）元组 数组
jy1=list(jy.items())
mp.sort(key= lambda x:x[1], reverse = True)  #降序
for i in range(20):#获取前二十高频词
    m[mp[i][0]]=mp[i][1]
list1=list(m.keys())
list2=list(m.values())
Bar().add_xaxis(list1).add_yaxis("政府工作报告2021图",list2).render("统计图2021.html")
print("{}:{}".format(jy1[0][0],jy1[0][1])) #显示2021的教育
#----------2022------------------------
for z2 in zf2:
    k2=jieba.lcut(z2, cut_all = True)   #全模式切分，
    for c2 in k2:
        if len(c2)==2:
            mk1[c2] = mk1.get(c2,0) + 1   #获取键值对,有这项加一 没这项给值填0                               
        if c2.count("教育")!=0:
            au[c2] = au.get(c2,0) + 1


qp = list(mk1.items())#item函数 以列表形式返回可遍历的（键,值）元组 数组
au1=list(au.items())
qp.sort(key= lambda x:x[1], reverse = True)  #降序
for i in range(20):#获取前二十高频词
    k[qp[i][0]]=qp[i][1]
list3=list(k.keys())
list4=list(k.values())
Bar().add_xaxis(list3).add_yaxis("政府工作报告2022图",list4).render("统计图2022.html")
print("{}:{}".format(au1[0][0],au1[0][1])) #显示2022的教育
