n = int(input())
a = list(map(int, input().split()))

num_dict = {}
for i in range(n):
    if a[i] in num_dict:
        num_dict[a[i]] += 1
    else:
        num_dict[a[i]] = 1

num = 0
if n % 2 == 0:
    num = 1
else:
    if not 0 in num_dict:
        print(0)
        exit()       
    if num_dict[0] != 1:
        print(0)
        exit()
    num = 2

for i in range(n // 2):
    if not num in num_dict:
        print(0)
        exit()        
    if num_dict[num] != 2:
        print(0)
        exit()
    num += 2
mod = pow(10, 9) + 7
print(pow(2, n // 2, mod))
