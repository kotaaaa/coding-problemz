n = int(input())

if n % 2 == 1:
    print(0)
    exit()

# ten = 1
ans = n // 10
# for i in range(int(len(str(n))-1)):
    # ten *= 10
    # ans += (n // ten) # * (i+1)
#     # if n >= 5*pow(10,i+1):
#         # ans += 1
p5 = 5 * 10
while p5 <= n:
    ans += n // p5
    p5 *= 5
print(ans)

# 123456790123456805
# 124999999999999995