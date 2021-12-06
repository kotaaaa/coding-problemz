n,x = map(int,input().split())
a = list(map(int,input().split()))
val = 0
for i in range(n):
    if i % 2 != 0:
        val += a[i] - 1
    else:
        val += a[i]

if val <= x:
    print("Yes")
else:
    print("No")
    
