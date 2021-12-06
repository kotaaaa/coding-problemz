n,p = map(int, input().split())
a = list(map(int, input().split()))

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

even_cnt = 0
odd_cnt = 0
for i in a:
    if i % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

def cal_odd_ncr(n):
    i = 1
    ret = 0
    while i <= n:
        if i % 2 == 1:
            # print("n:",n,"i:",i, ncr(n,i))
            ret += ncr(n,i) 
        i += 1

    return ret

# print(odd_cnt, even_cnt)
# print(cal_odd_ncr(odd_cnt))

if p == 1:
    print(cal_odd_ncr(odd_cnt)*pow(2,even_cnt))
else:
    print(pow(2,n) - cal_odd_ncr(odd_cnt)*pow(2,even_cnt))


