n = int(input())
mod = pow(10, 9) + 7


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


num_dict = {}
for i in range(1, n + 1):
    for j in prime_decomposition(i):
        if j in num_dict:
            num_dict[j] += 1
        else:
            num_dict[j] = 1


ans = 1
for k, v in num_dict.items():
    ans *= v + 1
    ans %= mod
print(ans)
