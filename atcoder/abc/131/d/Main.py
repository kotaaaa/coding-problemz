n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a,b = [list(i) for i in zip(*ab)]

tuple_ab = list(zip(a,b))

sorted_ab = sorted(tuple_ab, key=lambda i: i[1])

time = 0
for i in sorted_ab:
    time += i[0]
    if time > i[1]:
        print("No")
        exit()

print("Yes")