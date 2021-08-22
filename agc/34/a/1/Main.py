n,a,b,c,d = map(int, input().split())
s = input()

for i in range(len(s)-1):
    if s[i] == '#' and s[i+1] == '#':
        print("No")
        exit()
    
if c < d:
    print("Yes")
    exit()

change_ok = False
for i in range(b+1,d-1):
    if s[i-1] == '.' and s[i+1] == '.':
        change_ok = True
        break

# print(s[c])


if change_ok:
    print("Yes")
    exit()

if s[d-2] == '#' or s[d] == '#' or abs(d-c) <= 1:
    print("No")
    exit()

# if s[b-2] == '#' or s[b] == '#':
    # print("Yes")

# else:
    # print("No")

print("Yes")
