import math
a,b = map(int,input().split())
for i in range(b-a+1,0,-1):
    x = math.ceil(a / i)
    y = math.floor(b / i)
    # print(x,y,i)
    if y - x >= 1:
        print(i)
        exit()



# def gcd (a,b):
#     """a,b の最大公約数, gcd
#     Args:
#         a (int): num
#         b (int): num
#     Returns:
#         int : a,bの最大公約数
#     """
#     while b:
#         a, b = b, a % b
#     return a

# print(gcd(a,b))