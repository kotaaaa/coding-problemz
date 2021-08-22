n = int(input())
a = list(map(int, input().split()))

change_bool = False
cnt = 0

for i in range(n):
    if change_bool:
        change_bool = False
        continue

    if a[i] == i+1:
        change_bool = True
        cnt += 1

print(cnt)