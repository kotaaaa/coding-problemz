n,m = map(int, input().split())
s = input()
t = input()

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
    """a,bの最小公約数
    Args:
        a (int): num
        b (int): num`
    Returns:
        int : a,bの最小公約数
    """
    return a * b // gcd (a, b)

gcd_num = gcd(n,m)
lcm_num = lcm(n,m)
# print(gcd_num)
# print(lcm_num)

n_num = lcm_num // n
m_num = lcm_num // m


# for i in [i for i in range(lcm_num) if i % (n_num*m_num) == 0]:
i = 0
while i < lcm_num:
    # print(i)
    if s[i//n_num] != t[i//m_num]:
        print(-1)
        exit()
    i += n_num*m_num

print(lcm_num)




