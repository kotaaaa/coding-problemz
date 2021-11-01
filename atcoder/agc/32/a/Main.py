n = int(input())
b = list(map(int, input().split()))

import copy

flow = []

def dfs(l): 
    if len(l) == 0:
        # print("flow ",flow)
        for i in range(len(flow)-1,-1,-1):
            print(flow[i])
        exit()
        # return 
    print(l)
    for i in range(len(l)):
        if l[i] != i+1:
            # print("Muri ",len(l),i+1)
            continue
        # l.remove(i)
        # l2 = copy.copy(l1)
        del l[i]
        flow.append(i+1)
        # print(l)
        dfs(l)
        del flow[-1]
        l.insert(i,i+1)
        # print(l)
        # return 0
    # return 0

dfs(b)
print(-1)
# print(flow)

