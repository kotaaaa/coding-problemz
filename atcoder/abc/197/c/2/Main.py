n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
    exit()
    
ans = pow(2,30)
for i in range(1,2**(n-1)):
    seperater = set()
    for j in range(n-1):
        if (i>>j)&1 == 1:
            seperater.add(j)
    # print(seperater)
    arr = []
    start = 0
    for s in seperater:
        arr.append(a[start:s+1])
        start = s+1
    arr.append(a[start:])
    # print(arr)
    xored = 0
    for each_arr in arr:
        num = 0
        for j in each_arr:
            num = (num | j)      
        # print("num", num, (xored ^ num))
        xored = xored ^ num
    ans = min(ans, xored)
    # for j in range(n-1):
print(ans)