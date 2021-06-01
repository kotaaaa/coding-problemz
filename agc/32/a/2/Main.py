n = int(input())
b = list(map(int, input().split()))

# for i in range(1,-1,-1):
    # print(i)

# exit()


path = []
def dfs (l):
    if len(l) == 0:
        # print(len(path))
        for i in range(len(path)-1,-1,-1):
            print(path[i])
        exit()
    # print(l,len(l))
    for i in range(len(l)-1,-1,-1):
        # print(i)
        if len(l) <= i:
            continue

        if l[i] == i+1:
            del l[i]
            path.append(i+1)
            dfs(l)
    # print("a")
    
dfs(b)

# if len(path) == len(b):
#     for i in range(len(path)-1,-1,-1):
#         print(path[i])
# else:
print(-1)