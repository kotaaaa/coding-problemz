x,y = map(int, input().split())

if x == y:
    print(x)
    exit()
if x == 0 and y == 1:
    print(2)
    exit()
if x == 1 and y == 0:
    print(2)
    exit()
if x == 1 and y == 2:
    print(0)
    exit()
if x == 2 and y == 1:
    print(0)
    exit()
if x == 2 and y == 0:
    print(1)
    exit()
if x == 0 and y == 2:
    print(1)
    exit()

