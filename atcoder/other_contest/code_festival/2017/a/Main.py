n,m,k = map(int, input().split())

num_list = set()
for i in range(m+1):
    num_list.add(i*n)

for i in range((m+1)//2):
    
    base = ((n*m - (i*n)) - (i*n)) // n
    # print(base)
    num = i*n
    for j in range(n+1):
        num_list.add(num)
        num += base
# print(num_list)

if k in num_list:
    print("Yes")
else:
    print("No")