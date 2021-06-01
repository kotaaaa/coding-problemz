n = int(input())
a = list(map(int,input().split()))
mod = pow(10,9) + 7

a = list(set(a))
a.sort()
# print(a)
ans = a[0]+1
# print("ans",ans)
for i in range(1,len(a)):
    ans *= (a[i] - a[i-1] + 1)
    ans %= mod
    # print("ans",ans)
print(ans)