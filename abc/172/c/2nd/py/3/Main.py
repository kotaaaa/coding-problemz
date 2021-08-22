import math
import sys

n,m,k = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# ここから
# f = open("b9in.txt")  #19: 200000, 9: 113897
# l = f.readlines()
# n,m,k = map(int,l[0].split())
# a = [0] + list(map(int, l[1].split()))
# b = [0] + list(map(int, l[2].split()))
#  # ここまで

sum_a = [0 for i in range(n+1)]
sum_b = [0 for i in range(m+1)]

sum_a[0] = 0 # a[0]
for i in range(n):
    sum_a[i+1] += sum_a[i] + a[i]

sum_b[0] = 0 #b[0]
for i in range(m):
    sum_b[i+1] += sum_b[i] + b[i]

# print(sum_a)
# print(sum_b)

max_books = 0

def is_ok(n, tar):
    # 条件を満たすかどうか？問題ごとに定義
    return sum_b[n] <= tar

def meguru_bisect(ng, ok, tar):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, tar):
            ok = mid
        else:
            ng = mid
    return ok

# print(meguru_bisect(10**9 + 1, 0))
max_books = 0
for i in range(n+1):
    target = k - sum_a[i]
    if target < 0:
        break 
    # print(">> ",meguru_bisect(m + 1, 0, target))
    max_books = max(max_books, i + meguru_bisect(m + 1, 0, target))

print(max_books)