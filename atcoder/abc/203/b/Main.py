n,k = map(int, input().split())

sum_val = 0
for i in range(1,n+1):
    for j in range(1,k+1):
        sum_val += 100*i+j
print(sum_val)
