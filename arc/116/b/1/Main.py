

n = int(input())
a = list(map(int, input().split()))
a.sort()
s = [0 for i in range(n)]
s[n-1] = 1
mod = 998244353

for i in range(n-2,-1,-1):
    s[i] = (a[i] + 2*s[i+1]) % mod

print(s)
print(s[0])