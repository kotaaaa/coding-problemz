n = int(input())
a = list(map(int, input().split()))

# n = 1000000
# a = [0 for _ in range(n)]

val = 0
before = a[0]
all_0 = True
for i in a:
    if i != 0:
        all_0 = False
        break
if all_0:
    print("Yes")
    exit()

if n % 3 != 0:
    print("No")
    exit()


num_dict = {}
for i in a:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

if 0 in num_dict.keys() and num_dict[0] == n//3:
    if len(num_dict) == 2:    
        print("Yes")
    else:
        print("No")
    exit()

if len(num_dict) != 3:
    print("No")
    exit()


val = 0
# for i in num_dict.keys():
e = list(set(a))
if e[0] ^ e[1] ^ e[2] != 0:
    print("No")
    exit()

for i in num_dict.keys():
    if num_dict[i] != n // 3:
        print("No")
        exit()
print("Yes")

#     # if before != i:
#         # all_same = False
#     # print(bin(i))
#     val = val ^ i
# # for i in a:
#     # print(bin(i))
#     # val = val ^ i
# # print(val)

# if all_same:
#     print("No")
#     exit()
#     print("Yes")
# else:
#     print("No")