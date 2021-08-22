k,a,b = map(int, input().split())

if k <= a-1:
    print(k+1)
    exit()
if b - a <= 2:
    print(k+1)
    exit()

times = (k-(a-1)) // 2 
if (k-(a-1)) % 2 == 1:
    print(a+times*(b-a)+1)
else:
    print(a+times*(b-a))
