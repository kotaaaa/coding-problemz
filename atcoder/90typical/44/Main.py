n, q = map(int, input().split())
a = list(map(int, input().split()))
t = [0 for _ in range(q)]
x = [0 for _ in range(q)]
y = [0 for _ in range(q)]
for i in range(q):
    t[i], x[i], y[i] = map(int, input().split())
    x[i] -= 1
    y[i] -= 1

zero = 0

for i in range(q):
    # print(zero, a)
    if t[i] == 1:
        a[(x[i] + zero) % n], a[(y[i] + zero) % n] = (
            a[(y[i] + zero) % n],
            a[(x[i] + zero) % n],
        )
    elif t[i] == 2:
        zero -= 1
        zero %= n
    else:
        print(a[(x[i] + zero) % n])
