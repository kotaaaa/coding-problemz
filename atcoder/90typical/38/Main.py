a,b = map(int,input().split())

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
    return a * b // gcd (a, b)


val = lcm(a,b)
if val > 10 ** 18:
    print("Large")
else:
    print(val)