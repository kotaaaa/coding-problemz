k = int(input())
# print(k ** (1/3))


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


# nums = divisor(k)
ans = 0
for i in divisor(k):
    for j in divisor(k // i):
        c = k // (i * j)
        if i <= j <= c:
            ans += 1
print(ans)
