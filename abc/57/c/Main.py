import math

n = int(input())
fab = n
# print(math.sqrt(n))
# print(int(math.sqrt(n)))
# print(int(math.sqrt(n)) + 1)
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i != 0:
        continue
    a = i
    b = n // i
    fab = min(fab, max(len(str(a)), len(str(b))))

print(fab)
