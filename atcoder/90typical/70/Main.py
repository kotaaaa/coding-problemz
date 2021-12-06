n =int(input()) 
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

x.sort()
y.sort()

mid_x = x[n // 2]
mid_y = y[n // 2]

val = 0
for i in range(n):
    val += abs(x[i] - mid_x)
    val += abs(y[i] - mid_y)
print(val)



