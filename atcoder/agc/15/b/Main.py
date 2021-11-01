s = input()

cnt = 0
for i in range(len(s)):
    if s[i] == 'U':
        cnt += i*2+len(s)-i-1
    else:
        cnt += i+(len(s)-i-1)*2

print(cnt)