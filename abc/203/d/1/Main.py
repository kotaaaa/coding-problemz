n, k = map(int, input().split())
a = [list(map(int, input().split())) for l in range(n)]
print(a)
chuo = (k * k) // 2
print(chuo)
pond = [0 for i in range(k * k)]
min_chuo = pow(10, 9) + 1
for i in range(n - k + 1):
    for j in range(n - k + 1):
        idx = 0
        for tate in range(k):
            for yoko in range(k):
                pond[idx] = a[tate + i][yoko + j]
                idx += 1
        pond.sort(reverse=True)
        print(min_chuo, pond[chuo],pond)
        min_chuo = min(min_chuo, pond[chuo])
print(min_chuo)