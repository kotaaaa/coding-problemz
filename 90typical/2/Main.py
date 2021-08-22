n = int(input())
# print(pow(2,18))
# print(pow(2,20))
if n % 2 == 1:
    print()
    exit()

ansz = []
for i in range(1,pow(2,n)):
    if bin(i).count("1") != n // 2:
        continue
    cnt1 = 0
    cnt0 = 0
    is_correct = True
    arr = format(i,'0'+str(n)+'b')
    for j in arr:
        if j == '1':
            cnt1 += 1
        else:
            cnt0 += 1
        if cnt1 > cnt0:
            is_correct = False
            break
    if is_correct:
        ansz.append(arr)

ansz.sort()

for i in ansz:
    for j in i:
        if j == '1':
            print(")",end="")
        else:
            print("(",end="")
    print()

