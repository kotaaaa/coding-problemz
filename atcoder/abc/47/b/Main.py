w,h,n = map(int, input().split())

x = [0] * n
y = [0] * n
a = [0] * n

for i in range(n):
    x[i], y[i], a[i] = map(int, input().split())

mass = [[True for _ in range(h)] for _ in range(w)]
for i in range(n):
    if a[i] == 1:
        for j in range(x[i]):
            mass[j] = [False for _ in range(h)]
    if a[i] == 2:
        for j in range(x[i],w):
            mass[j] = [False for _ in range(h)]
    if a[i] == 3:
        for j in range(w):
            for k in range(y[i]):
                mass[j][k] = False
    if a[i] == 4:
        for j in range(w):
            for k in range(y[i],h):
                mass[j][k] = False

cnt = 0
for i in range(w):
    for j in range(h):
        if mass[i][j]:
            cnt += 1

print(cnt)