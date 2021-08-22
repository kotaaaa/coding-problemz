n,p = map(int, input().split())

if n == 1:
    print(p)
    exit()

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
            n = n // i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

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

# nums = divisor(p)
# print(nums)
primes = prime_decomposition(p)
# print(primes)

num_dict = {}
for i in primes:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

# print(num_dict)

sorted_num_dict = sorted(num_dict.items(), key=lambda i: i[0],reverse=True)
# print(sorted_num_dict)

ans = 1
for k_,v_ in sorted_num_dict:
    if v_ >= n:
        # ans *= k_
        ans *= k_**(v_ // n)
print(ans)