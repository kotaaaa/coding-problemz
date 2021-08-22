import math
import sys

# print(type(range(10)))


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

print(permutation("abcde",""))
print(z)
print(len(z))
exit()

def getCharNGram(n,s):
    """[ngram を求める関数]
    Args:
        n ([type]): [description]
        s ([type]): [description]
    Returns:
        [type]: [description]
    """
    charGram = [''.join(s[i:i+n]) for i in range(len(s)-n+1)]
    return charGram

s = int(input())
if s < 10:
    if s % 8 == 0:
        print("Yes")
    else:
         print("No")
    exit()

if s < 100:
    if s % 8 == 0:
        print("Yes")
    else:
        # print(int(str(s)[1]+str(s)[0]))
        # print(int(str(s)[1]+str(s)[0]) % 8)
        if int(str(s)[1]+str(s)[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    exit()

hachiz = []
for i in range(1, 1000):
    if i % 8 == 0:
        if i == 8:
            hachiz.append(str(i)+"00")
            continue
        if i < 100:
            hachiz.append(str(i)+"0")
            continue
        hachiz.append(str(i)) 


print(getCharNGram(3,str(s)))
# print(hachiz)
ans = 0
for i in getCharNGram(3,str(s)):
    # print("i ",i)
    for j in hachiz:
        # print("j ",j)
        cnt = 0
        for k in range(3):
            if j[k] in i:
                cnt += 1
        if cnt == 3:
            ans += 1
# print(ans)
if ans > 0:
    print("Yes")
else:
    print("No")