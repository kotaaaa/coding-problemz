n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = pow(10, 9) + 7
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            cnt += 1

cnt *= k
cnt %= mod

num_dict = {}
for i in range(n):
    if a[i] in num_dict:
        num_dict[a[i]] += 1
    else:
        num_dict[a[i]] = 1

sorted_num_dict = sorted(num_dict.items(), key=lambda i: i[0],reverse=False)
# print(sorted_num_dict)
sum_val = 0
tmp = 0
for i in range(len(sorted_num_dict)-1):
    tmp += sorted_num_dict[i][1]

    sum_val += (tmp*sorted_num_dict[i+1][1])

# if sorted_num_dict[-1][1] > 1:
#     tmp += sorted_num_dict[-1][1]
#     sum_val += tmp 
# print(sum_val)

# v = ((sum_val - 1) * sum_val) // 2
cnt += sum_val * (((k - 1) * k) // 2)
cnt %= mod
print(cnt)
