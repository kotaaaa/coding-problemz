a,b = map(int,input().split())

ans = [] 

if a < b:
    b_num = b + 1 
    a_num = a
else:
    b_num = b
    a_num = a + 1

a_sum = 0
b_sum = 0

for i in range(a_num-1):
    ans.append(i+1)
    a_sum += i+1
for i in range(b_num-1):
    ans.append(-1*(i+1))
    b_sum += i+1

# print(a_sum,b_sum)
# print(ans)
if a < b:
    ans.append(b_sum - a_sum)
else:
    ans.append(-1*(a_sum - b_sum))

for i in ans:
    print(i,end=" ")
