n = int(input())
a, b, c = map(int, input().split())

x = 0
y = 0
min_val = 10001
for i in range(10000):
    if a*i > n:
        continue
    for j in range(10000 - i):
        # print(i,j,(n - (a * i + b * j)))
        if a * i + b * j > n:
            break
        coins = i+j+((n - (a * i + b * j)) // c)
        if (n - (a * i + b * j)) % c == 0 and coins < 10000 and coins >= 0:
            # print(i,j,(n - a * i + b * j) // c)
            min_val = min(min_val, coins)
print(min_val)