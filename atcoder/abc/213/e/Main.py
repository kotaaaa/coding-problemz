####################
###### 01DFS #######
####################

# deque でキューを扱う
from collections import deque

# 入力
h, w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] = list(input())

distance = [[10 ** 6 for i in range(w)] for i in range(h)]
confirmed = [[-1 for i in range(w)] for i in range(h)]

queue = deque()
queue.append((0, [0, 0]))

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
bomb = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
distance[0][0] = 0


while len(queue) > 0:
    target_cost, target = queue.popleft()
    if confirmed[target[0]][target[1]] == 1:
        continue
    confirmed[target[0]][target[1]] = 1
    for dy, dx in direction:
        next_y = target[0] + dy
        next_x = target[1] + dx
        if 0 <= next_y < h and 0 <= next_x < w:
            ## 道のときは，一つ前のマスのコスト(target_cost)をキューの前から入れる
            if mass[next_y][next_x] == ".":
                if target_cost < distance[next_y][next_x]:
                    distance[next_y][next_x] = target_cost
                    queue.appendleft((target_cost, [next_y, next_x]))
            ## 壁のときは，一つ前のマスのコスト(target_cost)をキューの後ろから入れる
            else:
                for i_y, i_x in bomb:
                    if 0 <= next_y + i_y < h and 0 <= next_x + i_x < w:
                        if (
                            confirmed[next_y + i_y][next_x + i_x] != 1
                            and target_cost + 1 < distance[next_y + i_y][next_x + i_x]
                        ):
                            distance[next_y + i_y][next_x + i_x] = target_cost + 1
                            queue.append(
                                (target_cost + 1, [next_y + i_y, next_x + i_x])
                            )
print(distance[h - 1][w - 1])
