############
## 順列全探索
############
import itertools

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
if m != 0:
    xy = [list(map(int, input().split())) for _ in range(m)]
    x, y = [list(i) for i in zip(*xy)]

g = [[1 for _ in range(n)] for _ in range(n)]

if m != 0:
    for frm, to in zip(x, y):
        g[frm-1][to-1] = 0
        g[to-1][frm-1] = 0

ans = 10**9
# print(a)
# print(g)
for i in itertools.permutations([i+1 for i in range(n)]):
    # print(i,ans)
    val = 0
    is_valid = True
    for j in range(n-1):
        if g[i[j]-1][i[j+1]-1] == 0:
            is_valid = False
            break
        val += a[i[j]-1][j]
    val += a[i[n-1]-1][n-1]
    if not is_valid:
        continue

    ans = min(ans,val)
if ans == 10**9:
    print(-1)
    exit()
print(ans)