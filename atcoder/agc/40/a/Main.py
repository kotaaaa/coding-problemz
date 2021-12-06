s = input()
# len(s)+1
nums = [0 for i in range(len(s)+1)]

cnt = 0
for i in range(len(s)-1):
    if s[i] == '>' and s[i+1] == '<':
        cnt = 0
        nums[i+1] = 0
        continue
    if s[i] == '<':
        cnt += 1
        nums[i+1] = cnt

# print(nums)

cnt = 0
for i in range(len(s)-1, -1, -1):
    # if i == len(s)-1:
    if s[i-1] == '>' and s[i] == '<':
        cnt = 0
        # nums[i+1] = 0
        continue
    if s[i] == '>':
        cnt += 1
        nums[i] = max(nums[i],cnt)

# print(nums)


if s[0] == '>':
    nums[0] = nums[1]+1

if s[len(s)-1] == '<':
    # print(nums[-1])
    # print(nums[-2])
    nums[-1] = nums[-2]+1
    
# print(nums)
# <>>><<><<<<<>>><
# 0<3>2>1>0<1<2>0<1<2<3<4<5>2>1>0<1
#  6+3+15+3+1

ans = 0
for i in nums:
    ans += i
print(ans)
# 0<1>0>-1>-2<-1<0>1<2<3<4<5<6>5>4>3<4