import math
import sys

s,k = input().split()
k = int(k)

z = []

def permutation (q, ans):
    """[文字列の順列の並び替えの列挙プログラム]
    Args:
        q ([String]): [description] ex: "abcd" 
        ans ([String]): [description] ex: "" 
    """
    if len(q) <= 1:
        z.append(ans + q)
    else:
        for i in range(len(q)):
            permutation(q[0:i]+q[i+1:], ans+ q[i])

permutation(s,"")
# print(z)
z.sort()
# print(z)

set_c = set()
cnt = 0
for i in z:
    if i in set_c:
        continue
    set_c.add(i)
    cnt += 1
    if cnt == k:
        print(i)