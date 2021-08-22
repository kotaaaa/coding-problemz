h, w = map(int, input().split())
inf = pow(10, 18)
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] = list(input())
dp = [[-1 * inf for _ in range(w)] for _ in range(h)]
dp[-1][-1] = 0

def get_score(t):
    if t == "+":
        return 1
    else:
        return -1

for i in range(h - 1, -1, -1):
    for j in range(w - 1, -1, -1):
        if i < h - 1:
            dp[i][j] = max(dp[i][j], get_score(mass[i + 1][j]) - 1 * dp[i + 1][j])
        if j < w - 1:
            dp[i][j] = max(dp[i][j], get_score(mass[i][j + 1]) - 1 * dp[i][j + 1])

if dp[0][0] > 0:
    print("Takahashi")
elif dp[0][0] == 0:
    print("Draw")
else:
    print("Aoki")
