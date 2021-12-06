n,m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
a,b = [list(i) for i in zip(*ab)]

can1 = []
can2 = []
for i in range(m):
    if a[i] == 1:
        can1.append(b[i])
    if b[i] == n:
        can2.append(a[i])

# print(set(can1) & set(can2))
if len(set(can1) & set(can2)) > 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")