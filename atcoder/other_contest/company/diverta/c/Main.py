n = int(input())
s = [input() for _ in range(n)]

ab = 0
a = 0
b = 0
ba = 0
for i in s:
    ab += i.count("AB")
    # print(ab)
    if i[0] == "B" and i[-1] == "A":
        ba += 1
        continue
    if i[0] == "B":
        b += 1
    if i[-1] == "A":
        a += 1

# print(a,b,ab,ba)

if a == b:
    if a == 0:
        print(ab + a + max(0, (ba - 1)))
    else:
        print(ab + a + ba)
else:
    if a == 0 and b == 0:
        print(ab + ba - 1)
    else:
        print(ab + min(a, b) + ba)
