k, t = map(int, input().split())
a = list(map(int, input().split()))

sum_val = 0
max_val = 0
for i in range(t):
    sum_val += a[i]
    max_val = max(max_val, a[i])
other = sum_val - max_val
print(max(max_val - other - 1,0))

