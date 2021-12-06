import math
import sys

n,m = map(int, input().split())
p = [int(input()) for _ in range(n)]
p.sort()

p_mul = p
for i in range(n):
    for j in range(i, n):
        if p[i]+p[j] < m:
            p_mul.append(p[i]+p[j])

# print(p_mul)
# p_set = list(set(p_mul))

p_set = [0] + p_mul# + list(set(p_mul))
p_set.sort()
# p_set.remove(1)
# print(p_set)

def is_ok(n, target):
    # 条件を満たすかどうか？問題ごとに定義
    return p_set[n] < target

max_score = 0
for i in p_set:
    # print(i)
    target = m - i

    if target < 0:
        continue
    # print(target)

    ok = 0
    ng = len(p_set)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, target):
            ok = mid
        else:
            ng = mid
    max_score = max(max_score, p_set[ok] + i)

print(max_score)