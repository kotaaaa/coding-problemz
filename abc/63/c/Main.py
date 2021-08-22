n = int(input())

s = [int(input()) for _ in range(n)]

s.sort()
# print(s)

sum_record = 0
for i in s:
    sum_record += i

if sum_record % 10 != 0:
    print(sum_record)
    exit()

for i in s:
    if i % 10 != 0:
        print(sum_record - i)
        exit()

print(0)

