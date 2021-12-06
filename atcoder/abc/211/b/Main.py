s = [input() for _ in range(4)]
sz = set()
for i in range(4):
    sz.add(s[i])

if len(sz) == 4:
    print("Yes")
else:
    print("No")