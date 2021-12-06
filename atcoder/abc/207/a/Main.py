a,b,c,d = map(int,input().split())

num = a + b 
if a + c > num:
    num = a+c
if b + c > num:
    num = b+c
print(num)