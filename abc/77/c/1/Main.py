import math
import sys

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

# print(a)
# print(b)
# print(c)

def is_ok_b(n, target):
    # 条件を満たすかどうか？問題ごとに定義
    return b[n] > target

def is_ok_c(n, target):
    # 条件を満たすかどうか？問題ごとに定義
    return c[n] > target

ans = 0
frombtoc = [-1 for i in range(n)]

for i in range(n):
    ok = 0
    ng = n
    if a[i] > b[0]:
        continue
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok_b(mid, a[i]):
            ok = mid
        else:
            ng = mid
    # print("ok ", a[i], ok, b[ok])

    b_tmp_idx = ok
    # b_tmp = b[ok]
    for j in range(b_tmp_idx+1):

        if frombtoc[j] != -1:
            ans += frombtoc[j]
            continue

        # b_each_tmp = b[j]
        if b[j] > c[0]:
            continue

        ok = 0
        ng = n
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok_c(mid, b[j]):
                ok = mid
            else:
                ng = mid
        # print("ok c ", b_tmp, ok, c[ok], ((b_tmp_idx+1)*(ok+1)))
        # print("ok c ", b[j], ok, c[ok])
        frombtoc[j] = ok+1
        ans += ok+1
    # ans += (b_tmp_idx+1)*(ok+1)

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
