import numpy as np
import math 

n = int(input())
x,y = map(int, input().split())
x_n2,y_n2 = map(int, input().split())

med = ((x+x_n2)/2,(y+y_n2)/2)

lens = math.sqrt((x_n2-x)*(x_n2-x) +(y_n2-y)*(y_n2-y))/2

xz = []
yz = []

# deg = math.atan((y_n2-y)/(x_n2-x))
deg = math.atan2((y_n2-y),(x_n2-x))
# print("deg",math.degrees(deg))
for i in range(n):
    xz.append(np.cos(2*np.pi*i/n + deg)*lens)
    yz.append(np.sin(2*np.pi*i/n + deg)*lens)


# print(xz,yz)
print(xz[n//2+1]+med[0],yz[n//2+1]+med[1])


