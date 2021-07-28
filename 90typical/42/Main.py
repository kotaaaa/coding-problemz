# 公式解説通り, dp
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/042.jpg

k = int(input())
mod = 10 ** 9 + 7

# 桁和が9の倍数でなければ9の倍数にならない
if k % 9 != 0:
    exit(print(0))

dp = [0] * (k + 1)
dp[0] = 1
for i in range(1,k+1):
    b = min(i,9)
    for j in range(1,b+1):
        dp[i] += dp[i-j]
        dp[i] %= mod
print(dp[k])