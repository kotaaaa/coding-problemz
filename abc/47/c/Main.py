s = input()

before = s[0]
cnt = 1
for i in range(len(s)):

    if before == s[i]:
        pass
    else:
        cnt += 1
        before = s[i]

print(cnt - 1)


