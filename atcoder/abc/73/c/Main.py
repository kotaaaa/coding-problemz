n = int(input())
a = [int(input()) for _ in range(n)]

# nums = [0 for i in range(pow(10,9)+1)]
nums = set()
ans = 0
for i in a:
    # if nums[i] == 0:
    #     nums[i] = 1
    #     ans += 1
    # else:
    #     nums[i] = 0
    #     ans -= 1
    if i in nums:
        nums.remove(i)
        ans -= 1
    else:
        nums.add(i)
        ans += 1
    # print(ans)   
print(ans)

