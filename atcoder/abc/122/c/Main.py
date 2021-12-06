n,q = map(int, input().split())
s = input()
lr = [map(int, input().split()) for _ in range(q)]
l, r = [list(i) for i in zip(*lr)]

ac_cnt = [0 for _ in range(n)]
for i in range(1,n):
    ac_cnt[i] += ac_cnt[i-1]
    if s[i-1] == 'A' and s[i] == 'C':
        ac_cnt[i] += 1

for i in range(q):
    print(ac_cnt[r[i]-1] - ac_cnt[l[i]-1])