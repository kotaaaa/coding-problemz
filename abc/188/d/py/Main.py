import math
import sys
import itertools

s = input()
ints = int(s)
if int(ints) < 10:
    if ints % 8 == 0:
        print("Yes")
    else:
         print("No")
    exit()

if ints < 100:
    if ints % 8 == 0:
        print("Yes")
    else:
        if int(str(ints)[1]+str(ints)[0]) % 8 == 0:
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

s_counts = [0 for i in range(10)]
for i in range(len(s)):
    s_counts[int(s[i])] += 1
ans = 0

for i in hachiz: # 125
    ok_bool = True
    num_counts = [0 for i in range(10)]
    for j in range(3): # 3
        num_counts[int(i[j])] += 1
    for k in range(0,10): # 10
        if s_counts[k] < num_counts[k]:
            ok_bool = False
            break
    if ok_bool:
        print("Yes")
        exit()

print("No")
    


