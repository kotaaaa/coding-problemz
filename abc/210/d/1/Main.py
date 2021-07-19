h,w,c = map(int,input().split())
a = [[0 for _ in range(w)] for _ in range(h)]
inf = 10**9
dp = [[inf for _ in range(w)] for _ in range(h)]
for i in range(h):
    a[i] = list(map(int,input().split()))
print(a)

min_a = inf
min_ai = 0
min_aj = 0
min_b = inf
min_bi = 0
min_bj = 0
for i in range(h):
    for j in range(w):
        dp[i][j] = m
        if a[min_ai][min_aj] + a[i][j] + c*(abs(i-min_ai) + abs(j-min_aj)) < 
        