s = int(input())
q = s//10**9
r = s%10**9
x1 = q+1
y2 = 10**9
y1 = 10**9-r
x2 = 1
if s==10**18:
    print(0,0,10**9,0,0,10**9)
else:
    print(0,0,x1,y1,x2,y2)