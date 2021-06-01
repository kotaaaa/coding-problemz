h, w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] = list(map(int, input().split()))
# print(mass)
row_sum = [0 for _ in range(w)]
col_sum = [0 for _ in range(h)]
for i in range(h):
    for j in range(w):
        row_sum[j] += mass[i][j]
        col_sum[i] += mass[i][j]
# print(row_sum)
# print(col_sum)
# ans = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        print(row_sum[j] + col_sum[i] - mass[i][j],end=" ")
    print()