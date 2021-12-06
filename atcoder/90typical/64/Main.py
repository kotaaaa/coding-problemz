n,q = map(int,input().split())
a = list(map(int,input().split()))
a = [0] + a
l = [0 for _ in range(q+1)]
r = [0 for _ in range(q+1)]
v = [0 for _ in range(q+1)]

for i in range(1,q+1):
    l[i],r[i],v[i] = map(int,input().split())
    # l[i] -= 1
    # r[i] -= 1

val = 0
a_diff = [0 for _ in range(n+1)]
for i in range(1,n):
    a_diff[i] = a[i+1] - a[i]
    val += abs(a_diff[i])

for i in range(1,q+1):
    mae = abs(a_diff[l[i]-1]) + abs(a_diff[r[i]])
    if l[i] >= 2:
        a_diff[l[i]-1] += v[i]
    if r[i] <= n-1:
        a_diff[r[i]] -= v[i]
    ato = abs(a_diff[l[i]-1]) + abs(a_diff[r[i]])
    val += (ato - mae)
    print(val)
    
# print(val)

    



