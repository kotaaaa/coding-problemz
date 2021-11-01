a,b = list(map(int,input().split()))
if a >= b:
    print(0)
    exit()
print(b -max(a -1,0))
