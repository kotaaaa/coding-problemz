n = int(input())
a = list(map(int, input().split()))

sum_val = 0
sum_all = 0
for i in range(n):
    sum_all += a[i]

# print(sum_all)

ans = pow(10,15)
for i in range(n-1):
    sum_val += a[i]
    # print(sum_all,sum_val)
    ans = min(ans, abs(2*sum_val-sum_all))

print(ans)