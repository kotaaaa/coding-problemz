n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a46 = [0 for _ in range(46)]
b46 = [0 for _ in range(46)]
c46 = [0 for _ in range(46)]

for i in range(n):
    a46[a[i] % 46] += 1
    b46[b[i] % 46] += 1
    c46[c[i] % 46] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += a46[i] * b46[j] * c46[k]
print(ans)




