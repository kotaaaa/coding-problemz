n = int(input())
a = list(map(int, input().split()))

cnt4 = 0
cnt2 = 0
for i in a:
    if i % 4 == 0:
        cnt4 += 1
        continue
    if i % 2 == 0:
        cnt2 += 1

if cnt4 >= n//2:
    print("Yes")
    exit()

# rest_cnt = (n // 2) - cnt4

if cnt2 >= n - 2*cnt4:
    print("Yes")
    exit()
print("No")