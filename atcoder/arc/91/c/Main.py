n,m = map(int, input().split())

if n == 1 and m == 1:
    print(1)
    exit()

if n == 1:
    print(m-2)
    exit()

if m == 1:
    print(n-2)
    exit()

if n == 2 or m == 2:
    print(0)
    exit()


print((n-2)*(m-2))
