############
## 幅優先探索
############

import queue

r, c = map(int, input().split())

mass = [[] for _ in range(r)]
for i in range(r):
    mass[i] =  list(input())

roads = []
for i in range(r):
    for j in range(c):
        if mass[i][j] == '.':
            roads.append((i,j))
        
# q = deque()
# print(roads)
# print(mass)
max_distance = 0
for sy, sx in roads:
    visited = [[0 for _ in range(c)] for _ in range(r)]
    q = queue.Queue()

    q.put((sy, sx))
    before = (sy, sx)
    # cnt = 0
    path = {}

    while not q.empty():
        target_y, target_x = q.get()
        # print(target_y, target_x)
        current = (target_y, target_x)
        # if target_y == gy-1 and target_x == gx-1:
            # break;
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
        # cnt += 1

    ans = 0
    # print("a")
    # print(path)
    for g in roads:
        current = g
        if current == (sy, sx): 
            continue
        # print("b")
        distance = 0
        while True:
            # print(current)
            current = path[current]
            distance += 1
            if current == (sy, sx):
                break
        if max_distance < distance:
            max_distance = distance


print(max_distance)