p = int(input())


def factorial(n):
    """階乗計算 n!
    Args:
        n ([int]]):

    Returns:
        [int]: [ans]
    """
    mod = pow(10, 9) + 7
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        ans %= mod
    return ans


i = 11
# while True:
#     if factorial(i) >= p:
#         break
#     i += 1
# print(i)

cnt = 0
while True:

    if p <= 0:
        break
    fact = factorial(i)
    # print(fact,i)
    while fact <= p:
        # print(fact,p,"aaa")
        p -= fact
        cnt += 1
        # continue
    i -= 1
print(cnt)

