n = int(input())
a = map(int, input().split())

num_dict = {}

for i in a:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

# print(num_dict)

cnt = 0
for i in num_dict.keys():
    if num_dict[i] >= i:
        cnt += num_dict[i] - i
    else:
        cnt += num_dict[i]


print(cnt)