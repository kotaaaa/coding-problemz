n,k  = map(int, input().split())

mod = 10**9 + 7
ans = 0
for i in range(k,n+2):
    a = (i*(2*n-i+1))/2  #% mod
    b = (i*(i-1))/2 #% mod
    ans = (ans + a - b + 1) % mod

print(int(ans % mod))
# n(n+1)/2 - (n-k)(n-k+1)/2