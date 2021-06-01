
#########################
# 二次元累積和， 二分探索
#########################
n, k = map(int, input().split())
a = [list(map(int, input().split())) for l in range(n)]
l = k*k // 2

def create_binary_table(mid):
    table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if a[i][j] > mid: # mid より大きい数値がk*k//2個存在していたら中央値の最小値はmid以下のいずれかになる．
                table[i+1][j+1] = 1
            else:
                table[i+1][j+1] = 0

    for i in range(n-1):
        for j in range(n):
            table[i+2][j+1] += table[i+1][j+1]

    for j in range(n-1):
        for i in range(n):
            table[i+1][j+2] += table[i+1][j+1]

    return table
def solve (mid):
    mass = create_binary_table(mid)
    print("mid",mid,mass)
    for i in range(n-k+1):
        for j in range(n-k+1):
            print("sum","i",i,"j",j,mass[i+k][j+k]+mass[i][j]-mass[i+k][j]-mass[i][j+k])
            if mass[i+k][j+k]+mass[i][j]-mass[i+k][j]-mass[i][j+k] <= l:
                return True
    return False
# ok ,,, ng > left: ok, right: ng (最大値を求める) < 典型01
# ng ,,, ok > left: ng, right: ok (最小値を求める) < 今回
right = pow(10, 9) # 条件を満たす右端
left = -1 # 条件を満たさない左端
while right - left > 1:
    mid = (right + left) // 2
    if solve(mid):
        print("solve yes")
        right = mid
        # left = mid
    else:
        print("solve no")
        left = mid
        # right = mid
# print(left)
print(right) # 最小値を求めるとき， 条件を満たすのは右側