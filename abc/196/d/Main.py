
h,w,a,b = map(int, input().split())

used = [[False for i in range(16)] for j in range(16)]
def dfs(i, j, a, b):
    if a < 0 or b < 0:
        return 0
    if j == w:
        j = 0
        i += 1
    if i == h:
        return 1
    if used[i][j]:
        return dfs(i, j+1, a, b)
    res = 0
    used[i][j] = True
    res += dfs(i,j+1,a,b-1)
    if j+1 < w and used[i][j+1] == False:
        used[i][j+1] = True
        res += dfs(i,j+1,a-1,b)
        used[i][j+1] = False
    if i+1 < h and used[i+1][j] == False:
        used[i+1][j] = True
        res += dfs(i,j+1,a-1,b)
        used[i+1][j] = False
    used[i][j] = False

    return res


ans = dfs(0,0,a,b)
print(ans)