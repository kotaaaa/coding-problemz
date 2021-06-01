from collections import deque

h, w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

all_white = True
for i in range(h):
    for j in range(w):
        if mass[i][j] == "#":
            start = (i,j)
            all_white = False
            break
    if not all_white:
        break
if all_white:
    print("Yes")
    exit()

visited = [[0 for _ in range(w)] for _ in range(h)]
visited[start[0]][start[1]] = 1
q = deque([start])
print(q)
direction = [(1,0),(0,1),(-1,0),(0,-1)]

while q:
    current = q.popleft()
    print(current)
    # if visited[current[0]][current[1]] == 1:
        # continue
    for d in direction:
        print("d",d)
        if current[0]+d[0] < 0 or current[0]+d[0] >= h or current[1]+d[1] < 0 or current[1]+d[1] >= w or visited[current[0]+d[0]][current[1]+d[1]]:
            continue
        if mass[current[0]+d[0]][current[1]+d[1]] == '#':
            visited[current[0]+d[0]][current[1]+d[1]] = 1
            q.append((current[0]+d[0],current[1]+d[1]))

for i in range(h):
    for j in range(w):
        if visited[i][j] == 0 and mass[i][j] == "#":
            print("No")
            exit()

print("Yes")
