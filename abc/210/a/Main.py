n,a,x,y = map(int,input().split())
if n <= a:
    print(n*x)
    exit()
print(a*x+(n-a)*y)