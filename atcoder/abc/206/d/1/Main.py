n = int(input())
a = list(map(int, input().split()))

num_set = set()
for i in range(n//2):
    if a[i] == a[n-i-1]:
        continue
    elif a[i] < a[n-i-1]:
        num_set.add((a[i],a[n-i-1]))
    else:
        num_set.add((a[n-i-1],a[i]))

unique_set = set()
for i,j in num_set:
    unique_set.add(i)
    unique_set.add(j)
# print(num_set)
# print(unique_set)
if len(num_set) == 0:
    print(0)
    exit()
# if len(num_set) == len(unique_set):
#     print(len(num_set)-1)
# else:
#     print(len(num_set))
print(min(len(num_set),len(unique_set)-1))