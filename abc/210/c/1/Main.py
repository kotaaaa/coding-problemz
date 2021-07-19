n,k = map(int,input().split())
c = list(map(int,input().split()))

# nums = set()
num_dict = {}

for i in range(k):
    if c[i] in num_dict:
        num_dict[c[i]] += 1
    else:
        num_dict[c[i]] = 1
    

ans = len(num_dict)
for i in range(n-k):
    # print(nums)
    if c[i] in num_dict:
        # nums.remove(c[i]/)
        num_dict[c[i]] -= 1
        if num_dict[c[i]] ==0:
            del num_dict[c[i]]
    if c[i+k] in num_dict:
        num_dict[c[i+k]] += 1
    else:
        num_dict[c[i+k]] = 1
    ans = max(len(num_dict),ans)

print(ans)


    
