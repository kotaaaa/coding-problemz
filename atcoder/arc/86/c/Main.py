n,k = map(int, input().split())
a = list(map(int, input().split()))

nums = {}
for i in a:
    # print(i,nums)
    if i in nums:
        nums[i] += 1
    else:
        nums[i] = 1

# print(nums)

sorted_nums = sorted(nums.items(), key=lambda x:x[1]) #, reverse=True)

# print(sorted_nums)
# print(sorted_nums[0])
# print(sorted_nums[1])

ans = 0
for i in range(len(sorted_nums)-k):
    ans += sorted_nums[i][1]
print(ans)
