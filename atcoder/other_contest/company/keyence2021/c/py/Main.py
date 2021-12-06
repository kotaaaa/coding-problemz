import math
import sys
# import collections
# from heapq import heappop, heappush

H,W,K = map(int,input().split())
# mass = [list(map(int, input().split())) for _ in range(k)]
mass = [[[] for i in range(W+1)] for j in range(H+1)]
hw = []

mod = 998244353

for i in range(K):
    h,w,k=input().split()
    hw.append([int(h), int(w)])
    mass[int(h)][int(w)] = k

print(hw)
print(mass)

po = pow(3, H*W-K, mod)
print("po",po)

dp = [[0 for i in range(W+1)] for j in range(H+1)]

dp[1][1] = po
print(dp)

for i in range(1,H+1):
    for j in range(1,W+1):
        print(i,j,dp[i][j])
        # print(
        # print(dp[i+1][j])
        if i == H and j == W:
            break
        if mass[i][j] == 'X':
            if (i + 1 <= H):
                dp[i+1][j] += dp[i][j] % mod
            if (j + 1 <= W):
                dp[i][j+1] += dp[i][j] % mod
        elif mass[i][j] == 'D':
            if (i + 1 <= H):
                dp[i+1][j] += dp[i][j] % mod
        elif mass[i][j] == 'R':
            if (j + 1 <= W):
                dp[i][j+1] += dp[i][j] % mod
        else:
            if (i + 1 <= H):
                dp[i+1][j] += 2*dp[i][j] * (2/3) % mod
            if (j + 1 <= W):
                dp[i][j+1] += 2*dp[i][j] * (2/3) % mod            

print(dp[H][W])

