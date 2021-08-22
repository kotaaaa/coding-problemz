#########################
# いい感じに基本形の幅優先探索
# collections, deque を使う．
#########################


from collections import deque
h, w = map(int, input().split())

mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

sharp_cnt = 0
for i in range(h):
    for j in range(w):
        if mass[i][j] == '#':
            sharp_cnt += 1


q = deque()
visited = [[(0,0) for _ in range(w)] for i in range(h)]
q.append((0,0))
cnt = 1
while q:
    target = q.popleft()
    if target[0] == h-1 and target[1] == w-1:
        break

    if target[0]+1 < h and mass[target[0]+1][target[1]] == '#':
        q.append((target[0]+1,target[1]))
        visited[target[0]+1][target[1]] = target

    if target[1]+1 < w and mass[target[0]][target[1]+1] == '#':
        q.append((target[0],target[1]+1))
        visited[target[0]][target[1]+1] = target

current = (h-1,w-1)
while True:
    current = visited[current[0]][current[1]]
    cnt+=1
    if current == (0,0):
        break

if cnt == sharp_cnt:
    print("Possible")
else:
    print("Impossible")