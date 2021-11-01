h, w, k = map(int, input().split())

mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] = list(input())

cut_mass = [[0 for _ in range(w)] for _ in range(h)]
line1_empty = False

all_ichigo_cnt = 1
for i in range(h):
    ichigo_cnt = 0
    for j in range(w):
        if mass[i][j] == "#":
            if ichigo_cnt == 0:
                for k in range(j):
                    cut_mass[i][k] = all_ichigo_cnt
                ichigo_cnt += 1
            else:
                all_ichigo_cnt += 1
        cut_mass[i][j] = all_ichigo_cnt
    if ichigo_cnt == 0:
        # if i > 0:
        for k in range(w):
            cut_mass[i][k] = cut_mass[i-1][k]
        # else:
            # line1_empty = True
    else:
        all_ichigo_cnt += 1

for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if cut_mass[i][j] == 0:
            cut_mass[i][j] = cut_mass[i+1][j]

# if line1_empty:
#     for k in range(w):
#         cut_mass[0][k] = cut_mass[1][k]
# print(cut_mass)
for i in range(h):
    for j in range(w):
        print(cut_mass[i][j],end=" ")
    print()
