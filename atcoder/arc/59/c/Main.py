n = int(input())
a = list(map(int,input().split()))

min_a = 101
max_a = 0
for i in a:
    min_a = min(min_a,i)
    max_a = max(max_a,i)

min_val = pow(10,9)
for i in range(min_a,max_a+1):
    val = 0
    for j in a:
        val += (i-j)**2
    min_val = min(min_val,val)


print(min_val)