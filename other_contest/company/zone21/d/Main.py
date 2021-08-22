from collections import deque
s = input()

# str_s = []
str_s = deque()
# str_s.append(s[0])
reverse = False

for i in range(len(s)):
    # print(''.join(str_s))
    if s[i] == 'R':
        reverse = not reverse
        continue
    if reverse:
        # str_s.insert(0,s[i])
        str_s.appendleft(s[i])
        if len(str_s) < 2:
            continue
        if str_s[0] == str_s[1]:
            # print(''.join(str_s), "before")
            str_s.popleft()
            str_s.popleft()
            # print(''.join(str_s), "after")
    else:
        str_s.append(s[i])
        if len(str_s) < 2:
            continue
        if str_s[-1] == str_s[-2]:
            str_s.pop()
            str_s.pop()
    
if reverse:
    str_s.reverse()
print(''.join(str_s))