n = int(input())
a = list(map(int, input().split()))

ans = pow(2,30)
for i in range(1,n):
    print(a[:i],a[i:])
    left = 0
    for j in a[:i]:
        left = (left | j)
    right = 0
    for j in a[i:]:
        right = (right | j)
    
    ans = min(ans, left ^ right)
    print(left,right, left ^ right, ans)

print(ans)