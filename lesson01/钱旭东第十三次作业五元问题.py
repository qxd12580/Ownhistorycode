count = 0
#设有x个一员，y个五角，z个一角
for x in range(1,5):  # 最多五个一员
    for y in range(1,10):# 最多十个五角
        z=50-10*x-5*y
        if  z>0 and z+10*x+5*y==50:
            count+=1
            print('='*60)
            print(f'第{count}种买法,一员需要{x}个，五角需要{y}个，一角需要{z}个')
