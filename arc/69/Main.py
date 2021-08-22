n,m = map(int, input().split())

if 2*n >= m:
    print(m//2)
    exit()


rest_c = m-2*n
# print(rest_c)
print(n+rest_c//4)
