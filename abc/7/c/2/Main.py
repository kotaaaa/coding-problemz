############
## 幅優先探索
############

import queue
from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

mass = [[] for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    mass[i] =  list(input())

# q = deque()
q = queue.Queue()

q.put((sy-1, sx-1))
before = (sy-1, sx-1)
cnt = 0
path = {} 

while q:
    target_y, target_x = q.get()
    current = (target_y, target_x)
    if target_y == gy-1 and target_x == gx-1:
        break;
    if visited[target_y][target_x] == 1:
        continue
    visited[target_y][target_x] = 1
    current = (target_y, target_x)
    # right 
    if target_x + 1 < c and mass[target_y][target_x + 1] == '.' and visited[target_y][target_x + 1] == 0:
        # print((target_y, target_x + 1))
        q.put((target_y, target_x + 1))
        path[(target_y, target_x + 1)] = current
    # up 
    if target_y - 1 >= 0 and  mass[target_y-1][target_x] == '.' and visited[target_y-1][target_x] == 0:
        # print((target_y-1, target_x))
        q.put((target_y-1, target_x))
        path[(target_y - 1, target_x)] = current
    # left 
    if target_x - 1 >= 0 and mass[target_y][target_x - 1] == '.' and visited[target_y][target_x - 1] == 0:
        # print((target_y, target_x - 1))
        q.put((target_y, target_x - 1))
        path[(target_y, target_x - 1)] = current
    # down 
    if target_y + 1 < c and  mass[target_y+1][target_x] == '.' and visited[target_y+1][target_x] == 0:
        # print((target_y+1, target_x))
        q.put((target_y+1, target_x))
        path[(target_y + 1, target_x)] = current
    cnt += 1

ans = 0
while True:
    current = path[current]
    ans += 1
    if current == (sy-1, sx-1):
        break
# print(cnt)
print(ans)