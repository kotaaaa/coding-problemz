n,k = map(int,input().split())

nums = [0 for _ in range(k)]
res = 0
for i in range(1,n+1):
    nums[i%k] += 1
print(nums)
for a in range(k):
    b = (k-a) % k
    c = (k-a) % k
    print(a,b,c)
    if (b+c) % k != 0:
        continue
    res += nums[a] * nums[b] * nums[c]
print(res)