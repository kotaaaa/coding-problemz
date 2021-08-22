############
## 幅優先探索
############

import queue
from collections import deque

r, c = map(int, input().split())
mass = [[] for _ in range(r)]
for i in range(r):
    mass[i] =  list(input())

score = [[0 for _ in range(c)] for _ in range(r)]
# q = queue.Queue()
q = deque()

starts = []

for i in range(r):
    for j in range(c):
        if mass[i][j] == '#':
            starts.append((i,j))
            q.append((i,j))
            score[i][j] = 1

max_count = 0
while q:
    # target_y, target_x = q.get()
    target_y, target_x = q.popleft()
    # print(target_y+1, target_x+1)
    max_count = max(max_count, score[target_y][target_x])
    current = (target_y, target_x)
    # right 
    if target_x + 1 < c and score[target_y][target_x + 1] == 0:
        # print((target_y, target_x + 1))
        score[target_y][target_x + 1] = score[target_y][target_x] + 1
        q.append((target_y, target_x + 1))
        # max_count = max(max_count, score[target_y][target_x + 1])
    # up 
    if target_y - 1 >= 0 and score[target_y - 1][target_x] == 0:
        # print((target_y-1, target_x))
        score[target_y - 1][target_x] = score[target_y][target_x] + 1
        q.append((target_y-1, target_x))
        # max_count = max(max_count, score[target_y-1][target_x])
    # left 
    if target_x - 1 >= 0 and score[target_y][target_x - 1] == 0:
        # print((target_y, target_x - 1))
        score[target_y][target_x - 1] = score[target_y][target_x] + 1
        q.append((target_y, target_x - 1))
        # max_count = max(max_count, score[target_y][target_x - 1])
    # down 
    if target_y + 1 < r and score[target_y + 1][target_x] == 0:
        # print((target_y+1, target_x))
        score[target_y+1][target_x] = score[target_y][target_x] + 1
        q.append((target_y+1, target_x))
        # max_count = max(max_count, score[target_y+1][target_x])

# max_count = 0
# for i in range(r):
#     for j in range(c):
#         # print(score[i][j], end='')
#         max_count = max(max_count, score[i][j])
#     # print()
print(max_count-1)

