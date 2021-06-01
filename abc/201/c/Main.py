s = input()
maru = 0
batsu = 0
hatena = 0

for i in s:
    if i == "o":
        maru += 1
    elif i == "?":
        hatena += 1
    else:
        batsu += 1

ans = 0 
if maru > 4:
    print(0)
    exit()
if maru == 4:
    print(24)
    exit()
if maru == 3:
    ans = hatena * 24 + 36
    print(ans)
    exit()
if maru == 2:
    ans = 24 * (hatena * (hatena -1)) // 2 
    ans += hatena * 12 
    ans += 24 * hatena
    ans += 6 + 8
    print(ans)
    exit()
if maru == 0:
    ans = pow(hatena,4)
    print(ans)
    exit()
print(pow(hatena+1,4) - pow(hatena,4))
