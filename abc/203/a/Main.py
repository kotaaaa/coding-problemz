a, b, c = map(int, input().split())

if a == b:
    print(c)
    exit()
if a == c:
    print(b)
    exit()
if c == b:
    print(a)
    exit()

print(0)
