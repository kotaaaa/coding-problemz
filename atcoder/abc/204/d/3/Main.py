n = int(input())
t = list(map(int, input().split()))

# t.sort(reverse = True)
# print(t)

sum_val = 0
for i in t:
    sum_val += i

dp = [[True if i == 0 else False for i in range(sum_val+1)] for _ in range(n)]

for i in range(n-1):
    for k in range(sum_val+1):
        # i番目の数値を使うとき．
        dp[i+1][k] = dp[i][k-t[i]] or dp[i+1][k]
        # i番目の数値を使わないとき．
        dp[i+1][k] = dp[i][k] or dp[i+1][k]
# print(dp[n-1][sum])
# print(dp[n-1])
min_i = sum_val
for e,i in enumerate(dp[n-1]):
    if e < sum_val / 2:
        continue
    # print(i,e)
    if i:
        min_i = min(e,min_i)
print(min_i)
        