s = input()

cnt = 0
while len(s) > 0:
    if s[0] == s[-1]:
        s = s[1:-1]
        continue            
    if s[0] == "x" and s[-1] == "x":
        s = s[1:-1]
        continue
    if s[0] == "x":
        s = s + "x"
        cnt += 1
        continue
    if s[-1] == "x":
        s = "x" + s
        cnt += 1
        continue
    print(-1)
    exit()

print(cnt)