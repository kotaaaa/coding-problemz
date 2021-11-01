h, w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

rows = [False for i in range(h)]
cols = [False for i in range(w)]

for i in range(h):
    for j in range(w):
        if mass[i][j] == '#':
            rows[i] = True
            break

for j in range(w):
    for i in range(h):
        if mass[i][j] == '#':
            cols[j] = True
            break


for i in range(h):
    no_line_cnt = 0
    for j in range(w):
        # print(rows[i],cols[j], (rows[i] or cols[j]), (rows[i] and cols[j]))
        if rows[i] and cols[j]:
            print(mass[i][j],end="")
            no_line_cnt += 1
    if no_line_cnt > 0:
        print()

