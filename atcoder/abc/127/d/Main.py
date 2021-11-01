n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = [list(map(int, input().split())) for _ in range(m)]

a.sort(reverse=True)
# print(a)
sorted_bc = sorted(bc, key=lambda i: i[1], reverse=True)
# print(sorted_bc)

num = 0
ai = 0
bci = 0
sum_val = 0
while num < n:
    # print("bci",bci,"num",num)
    # print("sum_val",sum_val, a[ai],sorted_bc[bci][1])
    if bci >= m:
        # print("a")
        num += 1
        sum_val += a[ai]
        ai += 1
    elif a[ai] < sorted_bc[bci][1]:
        # print("b",bci)
        current_num = min(n - num, sorted_bc[bci][0])
        num += current_num
        sum_val += current_num * sorted_bc[bci][1]
        bci += 1
    elif a[ai] > sorted_bc[bci][1]:
        # print("c")
        sum_val += a[ai]
        num += 1
        ai += 1
    else:
        # print("d")
        # print(n - num,sorted_bc[bci][0] + 1, bci)
        current_num = min(n - num, sorted_bc[bci][0] + 1)
        num += current_num
        sum_val += current_num * sorted_bc[bci][1]
        bci += 1
        ai += 1
print(sum_val)