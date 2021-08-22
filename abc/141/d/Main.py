n,m = map(int,input().split())
a = list(map(int,input().split()))
a.append(0)
a.sort()
# print(a)
def solve (target, mid):
    return a[mid] < target

for i in range(m):
    target = a.pop()
    target = target // 2
    right = n
    left = 0
    while right - left > 1:
        mid = (right + left) // 2
        if solve(target,mid):
            left = mid
        else:
            right = mid
    a.insert(left+1, target)
    # print(left, a)
ans = 0
for i in a:
    ans += i
# print(a)
print(ans)