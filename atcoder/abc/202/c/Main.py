n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

num_dict = {}
for i in range(n):
    if a[i] in num_dict:
        num_dict[a[i]] += 1
    else:
        num_dict[a[i]] = 1
ans = 0
for i in range(n):
    if b[c[i]-1] in num_dict:
        ans += num_dict[b[c[i]-1]]
    
print(ans)