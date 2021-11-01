s = input()
maru = 0
batsu = 0
hatena = 0

ans = 0
for i in range(10000):
    nums = [0 for i in range(4)]
    for j in range(4):
        nums[j] = i % 10
        i //= 10
    # print(nums)
    isvalid = True
    for e,j in enumerate(s):
        if j == "o":
            if not e in nums:
                isvalid = False
                break
        if j == "x":
            if e in nums:
                isvalid = False
                break
    if isvalid:
        ans += 1

print(ans)