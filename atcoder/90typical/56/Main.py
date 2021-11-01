n,s = map(int,input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

dp = [[False for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = True

for i in range(1,n+1):
    for j in range(1,s+1):
        if j-b[i-1] >= 0 :
            dp[i][j] |= dp[i-1][j-b[i-1]]
        if j-a[i-1] >= 0 :
            dp[i][j] |= dp[i-1][j-a[i-1]]

if not dp[n][s]:
    exit(print("Impossible"))

ans = ""
before = s
for i in range(n-1,-1,-1):
    bool = True
    if s - a[i] >= 0:
        if dp[i][s - a[i]] == True:
            # print((before-j),a[i],b[i])
            ans += "A"
            s -= a[i]
            bool = False
    if s - b[i] >= 0 and bool:
        if dp[i][s - b[i]] == True:
            ans += "B"
            s -= b[i]
    
print(ans[::-1])
# dfs([n,s])

