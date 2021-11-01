n,D,H = map(int,input().split())
dh = [map(int, input().split()) for _ in range(n)]
d, h = [list(i) for i in zip(*dh)]

h_max = 0
for i in range(n):
    h_max = max(h_max, H-((H-h[i])/(D-d[i]))*D)

print(h_max)

