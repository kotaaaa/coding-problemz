h, n = map(int, input().split())
a = [0 for _ in range(n)]
b = [0 for _ in range(n)]

for i in range(n):
    a[i], b[i] = map(int, input().split())
inf = 10**9+1
# rate = [[i, 0] for i in range(n)]
# for i in range(n):
#     rate[i][1] = a[i] / b[i]

# sorted_rate = sorted(rate, key=lambda x: x[1], reverse=True)
# print(sorted_rate)
dp = [[inf for _ in range(h+1)] for i in range(n+1)]
for i in range(n):
    dp[i][0] = 0
for i in range(n):
    for j in range(h):
        # i番目の魔法を使わないとき
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        # i番目の魔法を使うとき
        dp[i+1][j] = min(dp[i+1][min(j+a[i],h)]+b[i], dp[i][j])
print(dp)
print(dp[n][h])


