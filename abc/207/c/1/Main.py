n = int(input())
t = [0 for _ in range(n)]
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]

for i in range(n):
    t[i],l[i],r[i] = map(int,input().split())

from operator import mul
from functools import reduce
def ncr(n,r):
    """ncr 計算 (import文 も必要)

    Args:
        n ([int]]): 
        r ([int]): 

    Returns:
        [int]: [description]
    """
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

# black_nums = [0 for _ in range(10**9+1)]
# white_nums = [0 for _ in range(10**9+1)]

nums = {}
for i in range(n):
    if t[i] == 1:
        if l[i] in nums:
            nums[l[i]] += 1
        else:
            nums[l[i]] = 1
        if r[i]+0.5 in nums:
            nums[r[i]+0.5] -= 1
        else:
            nums[r[i]+0.5] = -1
    elif t[i] == 2:
        if l[i] in nums:
            nums[l[i]] += 1
        else:
            nums[l[i]] = 1
        if r[i] in nums:
            nums[r[i]] -= 1
        else:
            nums[r[i]] = -1
    elif t[i] == 3:
        if l[i]+0.5 in nums:
            nums[l[i]+0.5] += 1
        else:
            nums[l[i]+0.5] = 1
        if r[i]+0.5 in nums:
            nums[r[i]+0.5] -= 1
        else:
            nums[r[i]+0.5] = -1
    elif t[i] == 4:
        if l[i]+0.5 in nums:
            nums[l[i]+0.5] += 1
        else:
            nums[l[i]+0.5] = 1
        if r[i]+0.5 in nums:
            nums[r[i]] -= 1
        else:
            nums[r[i]] = -1

sorted_nums = sorted(nums.items(), key=lambda i: i[0])
print(sorted_nums)
val = 0
ans = 0
for k,v in sorted_nums:
    val += v
    if val >= 2:
        ans += ncr(val,2)
print(ans)