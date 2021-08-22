

n = int(input())
a = list(map(int, input().split()))
times = [0 for i in range(401)]

ans = 0
sum_pow2 = 0 
for i in range(n):
    # print(a[i])
    # print(a[i]**2)
    sum_pow2 += a[i]**2
    times[a[i] + 200] += 1

# print("sum_pow2 ",sum_pow2)
# print(times)

ans += (n-1)*sum_pow2
print("ans",ans)
# print(times[208], times[204], times[202])
# for i in range(len(times)):
    # if times[i] != 0:
        # print(i-200, times[i])

# print("rrr")
# for i in range(400,-1,-1):
    # print(i)
# print("eee")

sum_mul = 0
for i in range(400,-1,-1):
    for j in range(400,i,-1):
        sum_mul += (i-200)*(j-200)*times[i]*times[j]
        # if times[i] != 0 and times[j] != 0:
            # print((i-200)*(j-200)*times[i]*times[j],"(i-200)*(j-200)*times[i]*times[j]", (i-200),(j-200),times[i],times[j], i-200,j-200)
print("sum_mul",sum_mul)
ans += -2*sum_mul
print(ans)


