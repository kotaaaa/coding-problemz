h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

mass = [[0 for _ in range(w)] for _ in range(h)]

cnt = 0
color = 0
for i in range(h):
    for j in range(w):
        cnt += 1
        mass[i][j] = color + 1
        if cnt == a[color]:
            cnt = 0
            color += 1

# print(mass)
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            print(mass[i][j],end=" ")
    else:
        for j in range(w-1,-1,-1):
            print(mass[i][j],end=" ")
    print()
