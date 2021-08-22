n = int(input())
a = list(map(int, input().split()))

a.sort() #reverse=True)

su = 0
ara = 0 

print(a)

sum_arr = 0
for i in range(n):
    sum_arr += a[i]

half = sum_arr // 2
print("half ",half)

i = -1
num = 0
while num <= half:
    i += 1
    num += a[i]

print("num 1",num)
while num > half:
    num -= a[i]
    i -= 1
    num += a[i]
    print("num 2",num)

print(i,num)


