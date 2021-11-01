n = int(input())
for i in range(1, 1000001):
    print(str(i) * 2)
    if int(str(i) * 2) > n:
        print(i - 1)
        exit()