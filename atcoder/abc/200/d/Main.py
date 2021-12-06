#########################
# bit全探索
# collections, deque を使う．
#########################
n = int(input())
a = list(map(int, input().split()))

def print_arr(arr):
    print(len(arr), end=" ")
    for each in arr:
        print(each, end=" ")
    print()

times = min(8,len(a))
nums = [[0,[]] for i in range(200)]
for i in range(1,pow(2,times)):
    target = []
    target_sum = 0
    for j in range(times):
        if (i>>j)&1 == 1:
            target.append(j+1)
            target_sum += a[j]
    if nums[target_sum % 200][0] == 0:
        nums[target_sum % 200][0] = 1
        nums[target_sum % 200][1] = target
    else:
        print("Yes")
        print_arr(target)
        print_arr(nums[target_sum % 200][1])
        exit()
print("No")