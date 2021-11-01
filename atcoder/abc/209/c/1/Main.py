n = int(input())
c = list(map(int,input().split()))

mod = 10**9 + 7

val = 1
c.sort()
for i in range(n):
    val *= c[i]-i
    val %= mod
print(val)
