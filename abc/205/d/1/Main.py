n, q = map(int, input().split())
a = list(map(int, input().split()))
k = [int(input()) for _ in range(q)]

nums = [0 for _ in range(n)]
for i in range(n):
    nums[i] = a[i] - i
# print(nums)


def solve(mid, target):
    if nums[mid] <= target:
        return True
    else:
        return False


for i in range(q):
    if nums[0] > k[i]:
        print(k[i])
        continue
    if nums[n - 1] < k[i]:
        print(a[n - 1] + (k[i] - nums[n - 1]) + 1)
        continue
    # print("aaa",k[i])
    right = n  ## ng min
    left = 0  ## ok max

    while right - left > 1:
        mid = (right + left) // 2
        # print("i>",i, left, right,"mid",mid)
        if solve(mid, k[i]):
            left = mid
        else:
            right = mid
    # print("left",left,"right",right,"k[i]",k[i])
    print(a[left] + 1)
    # print(a[left]+max((k[i]-nums[left],1)))


#
# 6 5
# 2 4 7 8 9 13
# 1
# 3
# 6
# 10
# 15
# 1,5,11,16,21