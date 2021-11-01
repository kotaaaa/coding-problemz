############
## 幅優先探索
############

import queue
r, c = map(int, input().split())
mass = [[] for _ in range(r)]
for i in range(r):
    mass[i] =  list(input())

roads = []
road_count = 0
wall_count = 0
for i in range(r):
    for j in range(c):
        if mass[i][j] == '.':
            roads.append((i,j))
            road_count += 1
        else:
            wall_count += 1
max_distance = 0
visited = [[0 for _ in range(c)] for _ in range(r)]
q = queue.Queue()

q.put((0, 0))
before = (0, 0)
path = {}

while not q.empty():
    target_y, target_x = q.get()
    # print(target_y, target_x)
    current = (target_y, target_x)
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
    if target_y + 1 < r and  mass[target_y+1][target_x] == '.' and visited[target_y+1][target_x] == 0:
        # print((target_y+1, target_x))
        q.put((target_y+1, target_x))
        path[(target_y + 1, target_x)] = current

ans = 0
current = (r-1, c-1)
distance = 0
if not current in path:
    print("-1")
    exit()
while True:
    current = path[current]
    distance += 1
    if current == (0, 0):
        break

print(r*c - (distance+1) - wall_count)