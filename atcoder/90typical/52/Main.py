n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

s = [0 for _ in range(n)]
mod = 10**9 + 7

ans = 1
for i in range(n):
    for j in range(6):
        s[i] += a[i][j]
    ans *= s[i]
    ans %= mod
print(ans)
