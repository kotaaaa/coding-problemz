h, w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

dp = [[0 for i in range(w)] for i in range(h)]
if mass[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0


for i in range(1,h):
    dp[i][0] = dp[i-1][0]
    if mass[i][0] == "#" and mass[i-1][0] == ".":
        dp[i][0] += 1
    
for j in range(1,w):
    dp[0][j] = dp[0][j-1]
    if mass[0][j] == "#" and mass[0][j-1] == ".":
        dp[0][j] += 1

for i in range(1,h):
    for j in range(1,w):

        if mass[i][j] == "#" and mass[i-1][j] == ".":
            from_up = dp[i-1][j] + 1
        else:
            from_up = dp[i-1][j]
    
        if mass[i][j] == "#" and mass[i][j-1] == ".":
            from_left = dp[i][j-1] + 1
        else:
            from_left = dp[i][j-1]
        dp[i][j] = min(from_up, from_left)
#         dp[i][j] = min(dp[i-1][j],dp[i][j-1])
#         if mass[i][j] == "#":
#             dp[i][j] += 1
print(dp[h-1][w-1])
