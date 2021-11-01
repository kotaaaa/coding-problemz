n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

cnt = 0
tmp_num = 0
for i in range(n-1,-1,-1):

    tmp_num += a[i]
    # print(tmp_num)
    if tmp_num % b[i] == 0:
        tmp_cnt = 0
    else:
        tmp_cnt = b[i] - (tmp_num % b[i])
    tmp_num -= a[i]
        
    tmp_num += tmp_cnt
    cnt += tmp_cnt

print(cnt)
