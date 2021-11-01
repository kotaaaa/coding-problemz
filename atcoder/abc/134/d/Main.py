n = int(input())
a = list(map(int, input().split()))

vals = [0 for _ in range(n)]
for i in range(n-1,-1,-1):
    baisu_cnt = 0
    for j in range(n // (i+1) - 1):
        # print("vals[(i+1)*(j+2)-1]",vals[(i+1)*(j+2)-1],(i+1)*(j+2)-1)
        baisu_cnt += vals[(i+1)*(j+2)-1]
    if baisu_cnt % 2 != a[i]:
        vals[i] = 1
    # print("i>>",i,baisu_cnt,a[i],vals[i])

# print(vals)
cnt1 = 0
for i in range(n):
    if vals[i] == 1:
        cnt1 += 1

print(cnt1)
if cnt1 == 0:
    exit()
for i in range(n):
    if vals[i] == 1:
        print(i+1,end=" ")


