n = int(input())
a = list(map(int, input().split()))
a = [i * 2 for i in a]
# print(a)

diff = 0
for i in range(n):
    if i % 2 == 0:
        diff += a[i]
    else:
        diff -= a[i]
# print(diff)

ansz = [0 for i in range(n)]
ansz[0] = diff // 2
for i in range(1, n):
    ansz[i] = a[i - 1] - ansz[i - 1]
# print(ansz)
for i in ansz:
    print(i, end=" ")
