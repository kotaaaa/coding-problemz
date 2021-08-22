n = int(input())
a = list(map(int, input().split()))

nums = [0 for i in range(pow(10,5)+2)]
# print(len(nums))
# print(nums)
max_num = 0
for i in a:
    nums[i] += 1
    max_num = max(max_num, i)
# print(max_num)

max_cnt = 0

max_cnt = max(max_cnt, nums[0])

for i in range(1,max_num+1):
    cnt = nums[i-1]+nums[i]+nums[i+1]
    # print(i,cnt)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
    

