n,k = map(int,input().split())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

val_dict = {}
for i in range(n):
    if a[i] in val_dict:
        val_dict[a[i]] += b[i]
    else:
        val_dict[a[i]] = b[i]

sorted_vals = sorted(val_dict.items(), key=lambda x:x[0])
# print(sorted_vals)
sum_val = 0
for key,v in sorted_vals:
    sum_val += v
    if k <= sum_val:
        print(key)
        exit()