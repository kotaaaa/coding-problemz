n = int(input())
d = list(map(int,input().split()))

nums = [0 for i in range(n)] 
for i in d:
    nums[i] += 1

mod = 998244353


if d[0] != 0:
    print(0)
    exit()
if nums[0] > 1:
    print(0)
    exit()

before = 1
ans = 1
# print(nums)
# print(nums[1:])
for i in nums[1:]:
    # print("i",i,ans,"before",before,pow(before, nums[i]))
    ans *= pow(before, i)
    ans %= mod
    before = i
print(ans)
