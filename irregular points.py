import math
R = 1.2802
theta = 0.1030

for i in range(61):
    #theta = theta * i
    x = R*math.cos(theta*i)
    y = R*math.sin(theta*i)
    print(i+195,":complex(",x,",",y,"),")