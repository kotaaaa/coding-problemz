n = int(input())
a = list(map(int, input().split()))
# a.sort(reverse=True)
# print(a)
amari200 = [0 for i in range(200)]
for i in a:
    amari200[i % 200] += 1

sum_val = 0
for i in range(200):
    k = amari200[i]
    if k >= 2:
        sum_val += k*(k-1)//2

print(sum_val)