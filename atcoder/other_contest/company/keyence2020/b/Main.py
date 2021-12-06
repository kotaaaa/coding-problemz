n = int(input())
xl = [map(int, input().split()) for _ in range(n)]
x, l = [list(i) for i in zip(*xl)]

st = [[0, 0] for _ in range(n)]
for i in range(n):
    st[i][0] = x[i] - l[i]
    st[i][1] = x[i] + l[i]

sorted_st = sorted(st, key=lambda x: x[1])
# print(sorted_st)

cnt = 1
before = sorted_st[0]
for i in range(1,n):
    if before[1] <= sorted_st[i][0]:
        before = sorted_st[i]
        cnt += 1
print(cnt)