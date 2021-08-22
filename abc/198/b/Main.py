n = input()

zero_cnt = 0
for i in range(len(n)-1,-1,-1):
    if n[i] == '0':
        zero_cnt += 1
    else:
        break


# print(zero_cnt)
# print((len(n)-zero_cnt // 2))

for i in range((len(n)-zero_cnt) // 2):
    if not n[i] == n[(len(n)-zero_cnt) - 1 - i]:
        print("No")
        exit()
print("Yes")
