n = int(input())
a = list(map(int, input().split()))

num_dict = {}
num_dict[a[0]] = 1
cnt = 1
ans = 0
for i in range(1,n):
    
    if a[i] in num_dict:
        ans += cnt - num_dict[a[i]]
        num_dict[a[i]] += 1
        
        # continue
    else:
        ans += cnt
        num_dict[a[i]] = 1
    cnt += 1
    # print(a[i],cnt,ans)
print(ans)
    