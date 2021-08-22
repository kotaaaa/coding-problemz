n,a,b = map(int,input().split())

import math, time
mod = 1000000007

def repeat_pow(x, n):
  ans = 1
  while(n > 0):
    if(bin(n & 1) == bin(1)):
      ans = ans*x
      ans %= mod
    x = x*x
    x %= mod
    n = n >> 1 #ビットシフト
  return ans

def cmb(n,a):
    over = 1
    start = time.time()
    for i in range(a):
        over = over * (n - i)
        over %= mod
    for i in range(2,a+1):
        over *= pow(i,-1,mod)
        over %= mod
    return over

ans = 0
start = time.time()
x = repeat_pow(2,n) % mod
y = cmb(n,a) % mod
z = cmb(n,b) % mod
w = 1
ans = x - y - z - w
ans %= mod

print(int(ans))