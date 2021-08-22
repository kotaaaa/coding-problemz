n,m = map(int,input().split())
xy = [map(int, input().split()) for _ in range(m)]
x, y = [list(i) for i in zip(*xy)]

red = [True if i == 0 else False for i in range(n)]
cnt = [1 for i in range(n)]
for i in range(m):
    cnt[x[i]-1] -= 1
    cnt[y[i]-1] += 1

    if red[x[i]-1]:
        red[y[i]-1] = True

    if cnt[x[i]-1] == 0:
        red[x[i]-1] = False
ans = 0
for i in range(n):
    if red[i]:
        ans += 1
# print(red)
print(ans)
