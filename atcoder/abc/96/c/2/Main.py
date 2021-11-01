from collections import deque

h, w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

direction = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(h):
    for j in range(w):
        if mass[i][j] == ".":
            continue
        adja_black = False
        for d in direction:
            if i+d[0] < 0 or i+d[0] >= h or j+d[1] < 0 or j+d[1] >= w:
                continue
            if mass[i+d[0]][j+d[1]] == '#':
                adja_black = True
                break
        if not adja_black:
            print("No")
            exit()
print("Yes")
