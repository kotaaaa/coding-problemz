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


def divisor(n): 
    """n の約数列挙
    Args:
        n (int): num
    Returns:
        約数のリスト
    """
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table


def prime_decomposition(n):
    """素因数分解
    Args:
        n (int): num
    Returns:
        [list]: nを素因数分解したリストを返す
    """
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


def is_prime(n):
    """素数判定
    Args:
        n ([int]): num
    Returns:
        [boolean]: 素数の場合: True, 素数でない場合: False
    """
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1



from operator import mul
from functools import reduce
def ncr(n,r):
    """ncr 計算 (import文 も必要)

    Args:
        n ([int]]): 
        r ([int]): 

    Returns:
        [int]: [description]
    """
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def factorial(n):
    """階乗計算 n!
    Args:
        n ([int]]): 

    Returns:
        [int]: [ans]
    """
    mod = pow(10,9)+7
    ans = 1
    for i in range(1,n+1):
        ans *= i
        ans %= mod
    return ans 
