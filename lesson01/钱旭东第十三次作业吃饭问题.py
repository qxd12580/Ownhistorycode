#设有x个男人，y个女人，z个小孩
count = 0
for x in range(1,17):#男人最多循环的次数
    for y in range(1,26):
        z=30-x-y
        if z>0 and 3*x+2*y+z==50:#满足这个条件即可
            count+=1
            print('='*60)#换行  
            print(f'第{count}种买法,男人有{x}个，女人有{y}个，小孩有{z}个')
            
