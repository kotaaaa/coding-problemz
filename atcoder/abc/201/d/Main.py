h, w = map(int, input().split())

mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())
dp = [[[0 for _ in range(2)] for _ in range(w)] for _ in range(h)]
# print(dp)
# dp[0][0][0]

for i in range(1,h):
    if i % 2 == 0:
        dp[i][0][1] = dp[i-1][0][1]
        fromup = dp[i-1][0][0]
        if mass[i-1][0] == "+":
            dp[i][0][0] = fromup + 1
        else:
            dp[i][0][0] = fromup - 1
    else:
        dp[i][0][0] = dp[i-1][0][0]
        fromup = dp[i-1][0][1]
        if mass[i-1][0] == "+":
            dp[i][0][1] = fromup + 1
        else:
            dp[i][0][1] = fromup - 1

for j in range(1,w):
    if j % 2 == 0:
        dp[0][j][1] = dp[0][j-1][1]
        fromleft = dp[0][j-1][0]
        if mass[0][j-1] == "+":
            dp[0][j][0] = fromleft + 1
        else:
            dp[0][j][0] = fromleft - 1
    else:
        dp[0][j][0] = dp[0][j-1][0]
        fromleft = dp[0][j-1][1]
        if mass[0][j-1] == "+":
            dp[0][j][1] = fromleft + 1
        else:
            dp[0][j][1] = fromleft - 1



for i in range(1,h):
    for j in range(1,w):
        if (i + j) % 2 == 0:
            dp[i][j][1] = max(dp[i][j-1][1],dp[i-1][j][1])
            fromleft = dp[i][j-1][0]
            if mass[i][j-1] == "+":
                fromleft += 1
            else:
                fromleft -= 1
            fromup = dp[i-1][j][0]
            if mass[i-1][j] == "+":
                fromup += 1
            else:
                fromup -= 1
            dp[i][j][0] = max(fromleft, fromup)
        else:
            dp[i][j][0] = max(dp[i][j-1][0],dp[i-1][j][0])
            fromleft = dp[i][j-1][1]
            if mass[i][j-1] == "+":
                fromleft += 1
            else:
                fromleft -= 1
            fromup = dp[i-1][j][1]
            if mass[i-1][j] == "+":
                fromup += 1
            else:
                fromup -= 1
            dp[i][j][1] = max(fromleft, fromup)
if (h-1+ w-1)%2 == 0:
    if mass[h-1][w-1] == "+":
        dp[h-1][w-1][0] += 1
    else:
        dp[h-1][w-1][0] -= 1
else:
    if mass[h-1][w-1] == "+":
        dp[h-1][w-1][1] += 1
    else:
        dp[h-1][w-1][1] -= 1


# print(dp)
if dp[h-1][w-1][1] > dp[h-1][w-1][0]:
    print("Aoki")
elif dp[h-1][w-1][1] < dp[h-1][w-1][0]:
    print("Takahashi")
else:
    print("Draw")