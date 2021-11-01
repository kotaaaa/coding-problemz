h, n = map(int, input().split())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]

for i in range(n):
    a[i], b[i] = map(int, input().split())
inf = 10**9+1
dp = [inf] * (h+1)
dp[0] = 0
# dp[a[i]] := モンスターに damage を与えるために必要な最小コスト
for i in range(h):
    for j in range(n):
        next_index = min(i + a[j],h)
        dp[next_index] = min(dp[next_index], dp[i] + b[j])
print(dp[h])