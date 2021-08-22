n,k,s = map(int, input().split())

max_const = pow(10,9)

if s == max_const:
    max_const -= 1

ans = [max_const for i in range(n)] 
for i in range(n):
    if i < k:
        ans[i] = s
    print(ans[i], end=" ")



