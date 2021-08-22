s = input()
t = input()

# for i in range(97, 123):
    # print(chr(i))



for i in range(97, 123):
    pair = ""
    for j in range(len(s)):
        if s[j] == chr(i):
            if pair != "":
                if t[j] != pair:
                    # print(s[j],t[j],pair)
                    print("No")
                    exit()
            else:
                pair = t[j]
                continue

for i in range(97, 123):
    pair = ""
    for j in range(len(s)):
        if t[j] == chr(i):
            if pair != "":
                if s[j] != pair:
                    # print(s[j],t[j],pair)
                    print("No")
                    exit()
            else:
                pair = s[j]
                continue

print("Yes")