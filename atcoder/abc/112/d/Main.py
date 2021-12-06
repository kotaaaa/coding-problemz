n, m = map(int, input().split())


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
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


nums = divisor(m)
ans = 1
for i in nums:
    if n > m // i:
        continue
    ans = max(ans, i)
print(ans)
