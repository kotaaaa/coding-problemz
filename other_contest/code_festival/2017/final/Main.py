s = input()

cnt_a = 0
cnt_b = 0
cnt_c = 0

for i in s:
    if i == 'a':
        cnt_a += 1
    if i == 'b':
        cnt_b += 1
    if i == 'c':
        cnt_c += 1

# print(cnt_a,cnt_b,c)
if abs(cnt_b - cnt_a) <= 1 and abs(cnt_c - cnt_a) <= 1 and abs(cnt_c - cnt_b) <= 1:
    print("YES")
else:
    print("NO")
