
a,b = map(int,input().split())

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

nums_a = set(prime_decomposition(a))
nums_b = set(prime_decomposition(b))

# print(nums_a)
# print(nums_b)

print(len(nums_a & nums_b)+1)