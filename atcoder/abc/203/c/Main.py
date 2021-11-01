n,k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
# a,b = [list(i) for i in zip(*ab)]

sorted_ab = sorted(ab, key=lambda i: i[0])
# print(sorted_ab)

current = k
for i in range(n):
    if sorted_ab[i][0] <= current:
        current += sorted_ab[i][1]
    else:
        break
print(current)
