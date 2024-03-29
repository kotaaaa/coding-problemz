from collections import deque
n, m = map(int, input().split())
# print()
# print(n)
# print(m)
# 隣接行列は作っておく
g = [[] for i in [0]*(n+1)]
# print(g)
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
def bfs(n, m, adj):
    visited = [0 for i in [0]*(n+1)]
    ans = 1
    for i in range(n+1):
        if visited[i]:
            continue
        Q = deque([i])
        group_friend = 1
        while Q:
            q = Q.popleft()
            visited[q] = 1
            link = adj[q]
            for j in link:
                if visited[j]:
                    continue
                visited[j] = 1
                group_friend += 1
                Q.append(j)
        ans = max(ans, group_friend)
    print(ans)
bfs(n, m, g)