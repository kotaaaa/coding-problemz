##############
### 尺取法 しゃくとり ###
##############

from collections import deque 
n,k = map(int,input().split())
a = list(map(int,input().split()))

q = deque()

num_dict = {}
kind = 0
ans = 0
for i in range(n):
    q.append(a[i])
    if a[i] in num_dict:
        num_dict[a[i]] += 1
    else:
        num_dict[a[i]] = 1
        kind += 1
    while kind > k:
        remove_num = q.popleft()
        # print(i,remove_num,q,num_dict)
        num_dict[remove_num] -= 1
        if num_dict[remove_num] == 0:
            del num_dict[remove_num]
            kind -= 1
    # print("q",q)
    ans = max(len(q),ans)
print(ans)
