n,k = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
# print(a)

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

gcd_num = a[0]
max_val = a[0]
for i in range(1,n):
    gcd_num = gcd(gcd_num,a[i])
    max_val = max(max_val,a[i])
if k <= max_val and k % gcd_num == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")