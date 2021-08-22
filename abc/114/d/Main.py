import math 

a,b,x = map(int,input().split())

if 0.5*a*a*b >= x:
    # print((2*x)/(a*b))
    print(math.degrees(math.atan2(b,((2*x)/(a*b)))))
# print(math.degrees(math.atan(b/((2*x)/(a*b)))))

else:
    print(math.degrees(math.atan((2/a)*(b - (x/(a*a))))))



