n = int(input())
t = list(map(int, input().split()))

t.sort(reverse = True)
print(t)

all = 0
s = [0 for _ in range(n)]
for i in range(n):
    all += t[i]
    s[i] = all

s = [0] + s
half_all = all / 2

right = 1
left = 0

sum_val = 0
ans = 0
print("half_all",half_all)
print(s)
while left < len(s) - 1:
    print("left,right",left,right)
    if left == right:
        print("right",right)
        right += 1
        continue
    if right >= len(s):
        left += 1
        sum_val = s[len(s)-1] - s[left]
        print("2 half_all",half_all,"sum_val",sum_val,"ans",ans)
        if abs(ans - half_all) > abs(sum_val - half_all):
            ans = sum_val
        # right -= 1
        continue
    # if right >= len(s):
        # sum_val = s[len(s)-1] - s[left]
    # else:
    sum_val = s[right] - s[left]
    print("half_all",half_all,"sum_val",sum_val)
    # if ans > abs(sum_val - half_all):
        # ans = abs(sum_val - half_all)
    if half_all > sum_val:
        # ans = sum_val
        right += 1
        # print("??",left,len(s) - 1)
    elif half_all < sum_val:
        # ans = sum_val
        left += 1    
    else:
        print(sum_val)
        exit()
    if abs(ans - half_all) > abs(sum_val - half_all):
        ans = sum_val
print(all - ans)
