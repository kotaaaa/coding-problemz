# from utils.util import divisor

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
            if i != 1:
                table.append(i)
            if n//i != 1:
                table.append(n//i)
        i += 1
    table = list(set(table))
    return table


a,b,c = map(int, input().split())

if c == 0:
    print("YES")
    exit()

if a % b == 0:
    print("NO")
    exit()
# print(divisor(a))
# print(divisor(b))
# print(divisor(c))
# print("a",set(divisor(a)) & set(divisor(b)))
yakusuu = 1
for i in set(divisor(a)) & set(divisor(b)):
    if i == b:
        break
    if i*yakusuu >= b:
        break
    yakusuu *= i
# print((set(divisor(a)) & set(divisor(b)) & set(divisor(c))))
# if yakusuu == 1:
#     yakusuu = 0
#     print("NO")
#     exit()

# print("yakusu", yakusuu)
# amaris = [i for i in range()]
# for i in range():
i = yakusuu
amaris = []
while (i < b):
    amaris.append(i)
    i += yakusuu

# print("b",amaris)
# if c % yakusuu == 0:
if c in amaris:
    print("YES")
else:
    print("NO")    

# if len((set(divisor(a)) & set(divisor(b)))) >= 1:
#     print("NO")
# else:
#     print("YES")


