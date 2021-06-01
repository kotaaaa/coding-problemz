n = int(input())
c = list(map(int,input().split()))

import sys 
sys.setrecursionlimit(100000)

max_color = 0
for i in c:
    max_color = max(max_color,i)

graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

colores = [0 for i in range(max_color+1)]
good_bool = [False for i in range(n+1)]
visited = [False for i in range(n+1)]

def dfs (x):
    
    delete_bool = False
    if visited[x]:
        return
    if colores[c[x-1]] == 0:
        delete_bool = True
        good_bool[x] = True
        colores[c[x-1]] += 1
    # print("colores1 x",x,colores)
    visited[x] = True
    for i in graph[x]:
        dfs(i)

    if delete_bool:
        colores[c[x-1]] -= 1
    # print("colores2 x",x,colores)

dfs(1)
for i in range(1,len(good_bool)):
    if good_bool[i]:
        print(i)
