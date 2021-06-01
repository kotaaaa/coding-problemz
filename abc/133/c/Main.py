l,r = map(int, input().split())

if r - l >= 2019:
    print(0)
    exit()
min_val = 2020
for i in range(l, r):
    for j in range(i+1,r+1):
        min_val = min(min_val, (i*j)%2019)
print(min_val)


# min_val = 2020
# max_val = 0
# min_i = 0
# min_j = 0
# max_i = 0
# max_j = 0

# for i in range(l,r):
#     for j in range(i+1,r):
#         print(i,j,(i*j) % 2019)
#         if min_val > (i*j) % 2019:
#             min_val = (i*j) % 2019
#             min_i = i
#             min_j = j
#         if max_val < (i*j) % 2019:
#             max_val = (i*j) % 2019
#             max_i = i
#             max_j = j
        # min_val = min(min_val, (i*j) % 2019)
        # max_val = max(max_val, (i*j) % 2019)
    # if i == 6:
        # exit()


# print(min_val, min_i, min_j)
# print(max_val, max_i, max_j)