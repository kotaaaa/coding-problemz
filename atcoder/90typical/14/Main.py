n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()

# print(a)
# print(b)

diff = [0] * n
sum_val = 0
for i in range(n):
    diff[i] = abs(a[i]-b[i])
    sum_val += diff[i]
print(sum_val)
