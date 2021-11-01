n = int(input())
a = list(map(int, input().split()))
a.sort()
sum_vals = [0 for _ in range(n)]
sum_vals[0] = a[0]
for i in range(1,n):
    sum_vals[i] = a[i] + sum_vals[i-1]
# print(a)
# print(sum_vals)

cnt = 0
for i in range(n-2,-1,-1):
    if 2*sum_vals[i] >= a[i+1]:
        cnt += 1
    else:
        break
print(cnt+1)