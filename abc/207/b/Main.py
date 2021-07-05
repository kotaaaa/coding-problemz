import math
a,b,c,d = map(int,input().split())

if d*c - b == 0:
    # if d == 1:
    print(-1)
        # exit()
    # if b == c:
        # print()
    
    exit()
x = a / (d*c-b)
if x < 0:
    print(-1)
    exit()
if x == 0:
    print(0)
    exit()
print(math.ceil(x))
