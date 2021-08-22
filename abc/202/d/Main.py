a, b, k = map(int, input().split())

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

# print(ncr(1,0))
# exit()
ab = a+b
s = ""
all_num = ncr(ab, b)
# print(all_num)
a_num = a-1
for i in range(1,ab+1):
    # print("ab-i",ab-i,"a_num",a_num,s)
    # if a-i < 0:
    if a_num <= -1:
        s += "b"
        continue
    if ab-i < a_num:
        s += "a"
        continue
    mid = ncr(ab-i, a_num)
    # print("ab-i",ab-i,"a_num",a_num,s,"mid",mid)
    # print("mid",mid)
    if k <= mid:
        # s = s.join("a")
        s += "a"
        a_num -= 1
    else:
        # s = s.join("b")
        s += "b"
        k -= mid
print(s)
