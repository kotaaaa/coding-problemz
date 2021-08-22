n = int(input())
s = input()
q = int(input())

t = [0] * q
a = [0] * q
b = [0] * q
s_idx = [i for i in range(2*n)]
for i in range(q):
    t[i], a[i], b[i] = map(int, input().split())

import copy

rev_bool = False
for i in range(q):
    if t[i] == 1:
        if rev_bool:
            if a[i] - 1 < n:
                tmp_a = s_idx[a[i] - 1 + n]
            else:
                tmp_a = s_idx[a[i] - 1 - n]
            if b[i] - 1 < n:
                tmp_b = s_idx[b[i] - 1 + n]
            else:
                tmp_b = s_idx[b[i] - 1 - n]

            if a[i] - 1 < n:
                s_idx[a[i] - 1 + n] = tmp_b
            else:
                s_idx[a[i] - 1 - n] = tmp_b
            if b[i] - 1 < n:
                s_idx[b[i] - 1 + n] = tmp_a
            else:
                s_idx[b[i] - 1 - n] = tmp_a
        else:
            tmp_a = s_idx[a[i] - 1]
            tmp_b = s_idx[b[i] - 1]
            s_idx[a[i] - 1] = tmp_b
            s_idx[b[i] - 1] = tmp_a

    else:
        if rev_bool:
            rev_bool = False
        else:
            rev_bool = True
if rev_bool:
    s_idx = s_idx[n:] + s_idx[:n]
for i in range(2*n):
    print(s[s_idx[i]],end="")