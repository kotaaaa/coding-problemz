s = input()
keyence = "keyence"

# cursol = 0
# for k in keyence:
    # s[cursol]

for i in range(len(s)):
    for j in range(i,len(s)):
        # print(s[:i]+s[j:])
        if s[:i]+s[j:] == keyence:
            print("YES")
            exit()
print("NO")