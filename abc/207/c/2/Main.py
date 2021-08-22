n = int(input())
t = [0 for _ in range(n)]
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]

for i in range(n):
    t[i],l[i],r[i] = map(int,input().split())

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if t[i] == 1:
            a = l[i]
            b = r[i]
        elif t[i] == 2:
            a = l[i]
            b = r[i]-0.1
        elif t[i] == 3:
            a = l[i]+0.1
            b = r[i]
        elif t[i] == 4:
            a = l[i]+0.1
            b = r[i]-0.1

        if t[j] == 1:
            c = l[j]
            d = r[j]
        elif t[j] == 2:
            c = l[j]
            d = r[j]-0.1
        elif t[j] == 3:
            c = l[j]+0.1
            d = r[j]
        elif t[j] == 4:
            c = l[j]+0.1
            d = r[j]-0.1

        if b >= c and a < d:
            cnt += 1
            continue
        if a <= d and c < b:
            cnt += 1
print(cnt)