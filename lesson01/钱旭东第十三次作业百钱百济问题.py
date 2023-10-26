#设买了x只公鸡，y只母鸡，z只小鸡
count = 0

for x in range(1,20):  #买了x只公鸡  100快最多20只
    for y in range(1,33):  #  买了 y只母鸡， 100快最多33只
        z=100-x-y
        if z>0 and 5*x+3*y+z/3==100:    #满足了这俩条件  即可
            
            count+=1
            print('='*60)
            print(f'第{count}种买法,公鸡买了{x}只，母鸡买了{y}只，小鸡买了{z}只')
