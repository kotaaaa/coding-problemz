n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_val = 1001
max_val = 0
for i in range(n):
    max_val = max(a[i], max_val)
    min_val = min(b[i], min_val)
# print(max_val,min_val)
print(max(min_val - max_val + 1,0))
