# import queue
from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

mass = [[] for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    mass[i] =  list(input())

# print(mass)

queue = deque()

queue.append((sy-1, sx-1))
before = (sy-1, sx-1)
cnt = 0
path = {} 

while queue:
    target_y, target_x = queue.pop()
    
    print(target_y+1, target_x+1)
    print(queue)
    current = (target_y, target_x)
    if target_y == gy-1 and target_x == gx-1:
        break;
    visited[target_y][target_x] = 1
    current = (target_y, target_x)
    # right 
    # print(mass[target_y][target_x + 1])
    # print(target_x + 1 < c)
    # print(mass[target_y][target_x + 1] == '.')
    # print(visited[target_y][target_x + 1] == 0)
    if target_x + 1 < c and mass[target_y][target_x + 1] == '.' and visited[target_y][target_x + 1] == 0:
        queue.append((target_y, target_x + 1))
        path[(target_y, target_x + 1)] = current
        cnt += 1
        # visited[target_y][target_x + 1] = 1
        continue
    # up 
    if target_y - 1 >= 0 and  mass[target_y-1][target_x] == '.' and visited[target_y-1][target_x] == 0:
        queue.append((target_y-1, target_x))
        # path[(target_y - 1, target_x)] = current
        cnt += 1
        visited[target_y - 1][target_x] = 1
        continue
    # left 
    if target_x - 1 >= 0 and mass[target_y][target_x - 1] == '.' and visited[target_y][target_x - 1] == 0:
        queue.append((target_y, target_x - 1))
        path[(target_y, target_x - 1)] = current
        cnt += 1
        # visited[target_y][target_x - 1] = 1
        continue
    # down 
    if target_y + 1 < c and  mass[target_y+1][target_x] == '.' and visited[target_y+1][target_x] == 0:
        queue.append((target_y+1, target_x))
        path[(target_y + 1, target_x)] = current
        cnt += 1
        # visited[target_y + 1][target_x] = 1
        continue
    # break
    # cnt += 1
# print("cnt",cnt)

ans = 0
while True:
    print("current ", current[0]+1, current[1]+1)
    current = path[current]
    ans += 1
    if current == (sy-1, sx-1):
        break

print("cnt",cnt)
print(ans)
