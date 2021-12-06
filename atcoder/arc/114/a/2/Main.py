import math
import copy

n = int(input())
x = list(map(int, input().split()))

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
candidates = []

for i in range(1,2**15):
    prime_set = set()
    for j in range(15):
        if (i>>j)&1 == 1:
            prime_set.add(prime[j])
    # print(prime_set)
    # so_bool = True
    ok_cnt = 0
    for j in x:
        # so_bool = False
        # if so_bool:
        for k in prime_set:
            if j % k == 0:
                # so_bool = True
                ok_cnt += 1
                break
    if ok_cnt == n:
        candidates.append(prime_set)
ans = 1
for i in prime:
    ans *= i

# print(candidates)
for i in candidates:
    muled = 1
    for j in i:
        muled *= j
    ans = min(ans, muled)
print(ans)

