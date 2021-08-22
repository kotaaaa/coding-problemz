n,k = map(int,input().split())
if n ==0:
    print(0)
    exit()
# if k == 0:
    # print()

visited = [-1 for _ in range(10**5)]
# visited[n] = 1
# mod = 10**5
cnt = 0
nums = [-1 for _ in range(10**5)]
nums[0] = n

cycle = -1
while True:
    # print("cnt>>",cnt,n,visited[n])
    if visited[n] >= 0:
        cycle = cnt - visited[n]
        break
    visited[n] = cnt
    nums[cnt] = n
    x = n
    for i in str(n):
        # print("x",x,i)
        x += int(i)
    n = x % (10**5)
    cnt += 1
    # nums[cnt] = n
    # visited[n] = 1

# print(cnt,cycle)
# print(nums[:cnt+4])
# print(nums[(k - (cnt - cycle)+1) % cycle])
# print(nums[(k - (cnt - cycle)) % cycle])
# print(nums[k % cycle])
# print(cnt,cycle,visited[n],"n",n)

if k < visited[n]:
    print(nums[k])
    exit()
print(nums[(k-visited[n]) % cycle + visited[n]])
# print(nums[9193])
# print(nums[9194])
# print(nums[9195])
