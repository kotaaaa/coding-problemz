n,a,b = map(int, input().split())

if b-a > n or b-a < 0:
    print(0)
    exit()

min_val = (n-1)*a + b
max_val = a + b*(n-1)

# print(min_val, max_val)

# print(max(max_val - (min_val - 1), 0))
print(max_val - (min_val - 1))