n = int(input())

if n == 1:
    print(0)
    exit()
if n == 2:
    print(1)
    exit()
val = 1
cnt =-1
while True:
    # print(val, cnt)
    if n < val:
        print(cnt)
        exit()
    val *= 2
    cnt += 1