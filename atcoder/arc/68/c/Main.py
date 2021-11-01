import math
x = int(input())
val = x % 11
if val == 0:
    print((x // 11)*2)
elif val >= 1 and val <= 6:
    print((x // 11)*2 + 1)
else:
    print((x // 11)*2 + 2)
