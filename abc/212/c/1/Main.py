n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

ans = 10**10

# print(a)
# print(b)

def solve (num, mid):
    return num > b[mid]
        # return True
    # else:
        # return False

for i in range(n):
    # ok ,,, ng > left: ok, right: ng (最大値を求める) < 典型01
    # ng ,,, ok > left: ng, right: ok (最小値を求める) < ABC203d
    right = m-1 # 条件を満たす右端
    left = -1 # 条件を満たさない左端
    val = 10 ** 10
    while right - left > 1:
        mid = (right + left) // 2
        if solve(a[i], mid):
            right = mid
        else:
            left = mid
    # print(right) # 最小値を求めるとき， 条件を満たすのは右側
    if right == 0:
        ans = min(abs(a[i] - b[0]),ans)
    elif right == m-1:
        ans = min(abs(a[i]- b[m-1]), ans)
    else:
        ans = min(abs(a[i]- b[right]), ans)
        ans = min(abs(a[i]- b[right-1]), ans)
print(ans)