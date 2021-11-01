w,h,x,y = map(int, input().split())

area = w*h/2

how = 1
if h/2 == y and w/2 == x:
    how = 1
else:
    how = 0

print(area,how)