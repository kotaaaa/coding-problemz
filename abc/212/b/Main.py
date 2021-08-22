s = input()

a = s[0]
same = True
for i in s:
    if i != a:
        same = False
        break
if same:
    print("Weak")
    exit()

num = int(s[0])
# order = True
for i in range(3):
    # print(int(s[i+1]), ((num + i+1) % 10))
    if int(s[i+1]) != ((num + i+1) % 10):
        print("Strong")
        exit()

print("Weak")