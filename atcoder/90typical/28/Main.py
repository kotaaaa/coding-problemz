####################
## 二次元いもす，累積和
####################
n = int(input())
lx = [0 for _ in range(n)]
ly = [0 for _ in range(n)]
rx = [0 for _ in range(n)]
ry = [0 for _ in range(n)]
for i in range(n):
    lx[i],ly[i],rx[i],ry[i] = map(int, input().split())

sums = [[0 for _ in range(1001)] for _ in range(1001)]
diff = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(n):
    diff[lx[i]][ly[i]] += 1
    diff[rx[i]][ry[i]] += 1
    diff[lx[i]][ry[i]] -= 1
    diff[rx[i]][ly[i]] -= 1

# x軸方向に累積和
for i in range(1,1001):
    for j in range(0,1001):
        diff[i][j] += diff[i-1][j]

# y軸方向に累積和
for i in range(0,1001):
    for j in range(1,1001):
        diff[i][j] += diff[i][j-1]

ans = [0 for _ in range(n+1)]
for i in range(1001):
    for j in range(1001):
        ans[diff[i][j]] += 1

for i in range(1,n+1):
    print(ans[i])