######################
### DFS  バックトラック ###
######################

h,w = map(int,input().split())

mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

visited = [[-1 for _ in range(w)] for _ in range(h)]
direction = [[-1,0],[0,1],[1,0],[0,-1]]
ans = 0

def dfs(sy,sx,py,px):
    if sy == py and sx == px and visited[py][px] == 1:
        return 0
    visited[py][px] = 1
    ret = -10000
    for dy,dx in direction:
        if 0 <= py+dy < h and 0 <= px+dx < w and mass[py+dy][px+dx] != '#':
            if visited[py+dy][px+dx] >= 0 and (sy != py+dy or sx != px+dx):
                continue
            v = dfs(sy,sx,py+dy,px+dx)
            ret = max(ret,  v + 1)
    visited[py][px] = -1
    return ret

for i in range(h):
    for j in range(w):
        ans = max(ans, dfs(i,j,i,j))
if ans <= 3:
    print(-1)
    exit()
print(ans)