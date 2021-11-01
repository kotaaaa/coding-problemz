c = [[] for i in range(3)]
for i in range(3):
    c[i] = (list(map(int, input().split())))

# print(c)
num = c[1][0] - c[0][0]
if num != c[1][1] - c[0][1] or num != c[1][2] - c[0][2]:
    print("No")
    exit()

num = c[2][0] - c[0][0]
if num != c[2][1] - c[0][1] or num != c[2][2] - c[0][2]:
    print("No")
    exit()

num = c[0][1] - c[0][0]
if num != c[1][1] - c[1][0] or num != c[2][1] - c[2][0]:
    print("No")
    exit()

num = c[0][2] - c[0][0]
if num != c[1][2] - c[1][0] or num != c[2][2] - c[2][0]:
    print("No")
    exit()

print("Yes")