n = int(input())
a = list(map(int, input().split()))

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

val = a[0]
for i in a:
    val = gcd(val, i)

print(val)