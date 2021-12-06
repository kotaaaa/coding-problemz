# from math import factorial

n,m = map(int,input().split())

mod = pow(10,9)+7

def factorial(k):
    """階乗計算 n!
    Args:
        n ([int]]): 

    Returns:
        [int]: [ans]
    """
    ans = 1
    for i in range(1,k+1):
        ans *= i
        ans = ans % mod
    return ans 

if abs(m - n) > 1:
    print(0)
    exit()
elif abs(m - n) == 1:
    print(factorial(m) % mod *factorial(n) % mod)
else:
    # min_val = min(m,n)
    print(factorial(n) *factorial(n) * 2 % mod)




