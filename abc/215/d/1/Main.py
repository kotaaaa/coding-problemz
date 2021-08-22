n,m = map(int,input().split())
a = list(map(int,input().split()))

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
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


nums = set()
for i in range(n):
    for j in prime_decomposition(a[i]):
        nums.add(j)
# print(nums)

vals = [1 for _ in range(m+1)]
vals[0] = 0
for i in nums:
    for j in range((m // i)):
        vals[i * (j+1)] = 0
cnt = 0
for i in vals:
    if i == 1:
        cnt += 1
print(cnt)
for i in range(m+1):
    if vals[i] == 1:
        print(i)

