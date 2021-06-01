n,m = map(int,input().split())

import sys 
sys.setrecursionlimit(100000)

graph = [[] for _ in range(m+1)]
for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



dfs()
