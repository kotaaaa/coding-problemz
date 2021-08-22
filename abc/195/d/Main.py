n,m,q = map(int,input().split())
wv = [map(int, input().split()) for _ in range(n)]
w, v = [list(i) for i in zip(*wv)]
x = list(map(int, input().split()))
lr = [map(int, input().split()) for _ in range(q)]
l, r = [list(i) for i in zip(*lr)]

ans = [0 for i in range(q)]

for i in range(q):
    # print(x[l[i]-1:r[i]])
    boxs = x[:l[i]-1]+x[r[i]:]
    boxs.sort()
    # print(w)
    # print(v)
    # print(boxs)
    used = [0 for i in range(len(boxs))]
    putted = [0 for i in range(len(w))]
    # print(sorted(range(len(v)), key=lambda k: v[k]))
    sorted_value = sorted(range(len(v)), key=lambda k: v[k], reverse=True)
    # print(sorted_value)
    # for j in range(len(w)):
        # print(w[sorted_value[j]])

    for j in range(len(w)):
        for idx,k in enumerate(boxs):
            if used[idx] == 1:
                continue
            if w[sorted_value[j]] <= k:
                used[idx] = 1
                putted[sorted_value[j]] = 1
                break
    
    # print("used ",used)
    # print("putted ",putted)
    for j in range(len(w)):
        if putted[j] == 1:
            ans[i] += v[j]
    # break

for i in ans:
    print(i)
# print(ans)
    # break


