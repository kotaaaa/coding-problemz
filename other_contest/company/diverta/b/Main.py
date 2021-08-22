r,g,b,n = map(int, input().split())

cnt = 0
# print(r,g,b,n)
for r_ in range(n+1):
    for g_ in range(n+1):
        # print("a",r_,g_,n - (r*r_+g*g_))
        if (n - (r*r_+g*g_)) % b != 0:
            continue
        b_ = (n - (r*r_+g*g_)) // b
        # print(r_,g_,b_)
        if b_ < 0:
            continue
        cnt += 1
print(cnt)