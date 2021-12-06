n = int(input())
a = list(map(int, input().split()))

minus_cnt = 0
min_abs = pow(10, 9) + 1
sum_val = 0
for i in a:
    if i < 0:
        minus_cnt += 1
    min_abs = min(min_abs, abs(i))
    sum_val += abs(i)

if minus_cnt % 2 == 0:
    print(sum_val)
else:
    print(sum_val - 2 * min_abs)
