n = int(input())
t = [int(input()) for i in range(n)]
# mod = pow(10,18)+1

def gcd (a,b):
    """a,b の最大公約数, gcd
    Args:
        a (int): num
        b (int): num
    Returns:
        int : a,bの最大公約数
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """a,bの最小公倍数
    Args:
        a (int): num
        b (int): num`
    Returns:
        int : a,bの最小公倍数
    """
    return a * b // gcd (a, b)  # % mod

num = t[0]
for i in range(1,n):
    num = lcm(num, t[i])

print(num)