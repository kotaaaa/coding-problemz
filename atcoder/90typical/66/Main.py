n = int(input())
lr = [map(int, input().split()) for _ in range(n)]
l, r = [list(i) for i in zip(*lr)]

ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        li, ri = l[i],r[i]
        lj, rj = l[j],r[j]
        cnt = 0
        for x in range(li, ri+1):
            for y in range(lj, rj+1):
                if x > y:
                    cnt += 1
        ans += cnt / ((ri - li + 1) *  (rj - lj + 1))
print(ans)
            


