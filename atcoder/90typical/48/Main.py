n,k = map(int,input().split())
ab = [map(int, input().split()) for _ in range(n)]
a,b = [list(i) for i in zip(*ab)]

nums = []
nums.extend(b)

for i in range(n):
    nums.append(a[i]-b[i])
nums.sort(reverse=True)

# print(nums)
ans = 0
for i in range(k):
    ans += nums[i]
print(ans)