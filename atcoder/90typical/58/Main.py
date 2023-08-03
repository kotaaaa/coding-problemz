n, k = map(int, input().split())
if n == 0:
    print(0)
    exit()

visited = [-1 for _ in range(10**5)]
cnt = 0
nums = [-1 for _ in range(10**5)]
nums[0] = n

cycle = -1
while True:
    if visited[n] >= 0:
        cycle = cnt - visited[n]
        break
    visited[n] = cnt
    nums[cnt] = n
    x = n
    for i in str(n):
        x += int(i)
    n = x % (10**5)
    cnt += 1

if k < visited[n]:
    print(nums[k])
    exit()
print(nums[(k - visited[n]) % cycle + visited[n]])
