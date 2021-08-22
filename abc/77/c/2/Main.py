import math
import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort() #reverse=True)
b.sort() #reverse=True)
c.sort(reverse=True)

# print(a)
# print(b)
# print(c)

def is_ok_a(n, target):
    # 条件を満たすかどうか？問題ごとに定義
    return a[n] < target

def is_ok_c(n, target):
    # 条件を満たすかどうか？問題ごとに定義
    return c[n] > target

ans = 0

for i in range(n):
    ok = 0
    ng = n
    if b[i] <= a[0]:
        continue
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok_a(mid, b[i]):
            ok = mid
        else:
            ng = mid
    # print("ok a ", b[i], a[ok], ok+1) # "a[",ok,"]",
    ok_a = ok 
    ok = 0
    ng = n
    # print("c")
    if b[i] >= c[0]:
        continue
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok_c(mid, b[i]):
            ok = mid
        else:
            ng = mid
    # print("ok c ", b[i], c[ok], ok+1) # "a[",ok,"]",
    ok_c = ok 
    ans += (ok_a+1) * (ok_c+1)

print(ans)
# def meguru_bisect(ng, ok, tar):
#     '''
#     初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
#     まずis_okを定義すべし
#     ng ok は  とり得る最小の値-1 とり得る最大の値+1
#     最大最小が逆の場合はよしなにひっくり返す
#     '''
#     while (abs(ok - ng) > 1):
#         mid = (ok + ng) // 2
#         if is_ok(mid, tar):
#             ok = mid
#         else:
#             ng = mid
#     return ok
