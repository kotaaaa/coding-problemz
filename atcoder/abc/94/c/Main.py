n = int(input())
a = list(map(int, input().split()))

# a_idx = [i for i in range(len(a))]
# sorted_idx = sorted(a_idx, key=lambda i : -a[i]) # 降順: -a[i], 昇順: a[i] #キーは，a[i]でソートするが，実際に，ソートされる配列は，a_idx（a_idxの値）
# sorted_a = [a[i] for i in sorted_idx]

a_dict = dict(zip([i for i in range(len(a))],a))

sorted_a = sorted(a_dict, key=lambda i :-a_dict[i])

sorted_a_val = sorted(a,reverse=True)

sorted_arr_key = dict(zip(sorted_a,[i for i in range(len(a))]))

for i in range(n):
    if sorted_arr_key[i] < n//2:
        print(sorted_a_val[n//2])
    else:
        print(sorted_a_val[n//2-1])
