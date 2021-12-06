# ref: https://atcoder.jp/contests/abc212/submissions/24729327

n,m,k = map(int,input().split())
mod = 998244353

# NG 
uv = [map(int, input().split()) for _ in range(m)]
# u, v = [list(i) for i in zip(*uv)]
g = [[] for _ in range(n)]
# for frm, to in zip(u, v):
for frm, to in uv:
    frm, to = frm-1, to-1
    g[frm].append(to)
    g[to].append(frm)
# NG ここまで

# OK
# g = [[] for _ in range(n)]
# for i in range(m):
#     u,v=map(int,input().split())
#     u,v=u-1,v-1
#     g[u].append(v)
#     g[v].append(u)
# OK ここまで

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
dp[0][0] = 1

for i in range(k):
    times = 0
    for j in range(n):
        times += dp[i][j]
    for j in range(n):
        dp[i+1][j] = times - dp[i][j]
        for adja in g[j]:
            dp[i+1][j] -= dp[i][adja]
        dp[i+1][j] %= mod
print(dp[k][0])
