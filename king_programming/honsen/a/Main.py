n = int(input())
a = list(map(int,input().split()))
s = [0 for _ in range(n+1)]
s[0] = 0
s[1] = a[0]
for i in range(1,n):
    s[i+1] = s[i] + a[i]

# print(s)
for i in range(1,n+1):
    val = 0
    for j in range(n-i+1):
        val = max(val,s[j+i] - s[j])
    print(val)





