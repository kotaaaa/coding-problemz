n,m = map(int, input().split())

ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

cd = [map(int, input().split()) for _ in range(m)]
c, d = [list(i) for i in zip(*cd)]

ans = [0 for i in range(n)]
for i in range(n):
    min_distance = 4*pow(10,8)
    min_index = 51
    for j in range(m):
        # print(a[i],c[j],b[i],d[j])
        if abs(a[i] - c[j])+abs(b[i] - d[j]) < min_distance:
            min_distance = abs(a[i] - c[j])+abs(b[i] - d[j])
            min_index = j+1
        
    ans[i] = min_index

for i in range(n):
    print(ans[i])