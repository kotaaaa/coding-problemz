#######################
### 拡張BFS
### https://twitter.com/094La50wJ8O5RaU/status/1408111511462051843?s=20
#######################

from collections import deque

h, w = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1
cs -= 1
rt -= 1
ct -= 1
s = [[] for _ in range(h)]
for i in range(h):
    s[i] = list(input())

dxdy = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
times = [[10 ** 9 for _ in range(w)] for _ in range(h)]

q = deque()
q.append([rs, cs, -1, -1])  # 座標y, 座標x, 向き, cost
times[rs][cs] = -1

turn = 0
while len(q) > 0:
    y, x, direction, cost = q.popleft()
    for dx, dy, direction2 in dxdy:
        if (0 <= x + dx < w) and (0 <= y + dy < h) and s[y + dy][x + dx] != "#":
            if direction != direction2:
                if times[y + dy][x + dx] < cost + 1:
                    continue
                times[y + dy][x + dx] = cost + 1
                q.append([y + dy, x + dx, direction2, cost + 1])
            else:
                if times[y + dy][x + dx] < cost:
                    continue
                times[y + dy][x + dx] = cost
                q.appendleft([y + dy, x + dx, direction2, cost])
print(times[rt][ct])