import math
import copy

n = int(input())
x = list(map(int, input().split()))

x.sort()
# filtered = []
# for i,val in enumerate(x):
#     for j in range(i+1, n):
#         if x[j]%val != 0:
#             filtered.append(i)

# filtered = list(set(filtered))
# print(filtered)
# # print(n)
# print(x)

# set = {}
set_yakusu = set()

for i in x:
    # print(int(math.sqrt(i)))
    # set_yakusu = set()
    # print(set_yakusu)
    
    break_flg = False
    for j in set_yakusu:
        # print(i,j)
        if i % j == 0:
            break_flg = True
    if break_flg:
        continue

    min_yakusu = 51
    for j in range(1,int(math.sqrt(i)+1)):
        if i % j == 0:
            if j != 1:
                # set_yakusu.add(j)
                yakusu = j
                min_yakusu = min(min_yakusu, yakusu)
            # set_yakusu.add(int(i / j))
            if i != j:
                yakusu = int(i/j)
                min_yakusu = min(min_yakusu, yakusu)
    set_yakusu.add(min_yakusu)

# print(set_yakusu)
ans = 1
for i in set_yakusu:
    ans *= i

# gcd_num = x[0]
# for i in x[1:]:
#     print(i, math.gcd(gcd_num, i))
#     if math.gcd(gcd_num, i) != 1:
#         gcd_num = math.gcd(gcd_num, i)
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

if len(x)>1:
    gcd_num = my_gcd(*x)
else:
    gcd_num = 1 
# print(gcd_num)
if gcd_num != 1:
    print(min(ans,gcd_num))
else:
    print(ans)
