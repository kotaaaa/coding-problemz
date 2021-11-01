n = int(input())
s = input()

max_size = 0
for i in range(1,n):
    # print(s[:i], s[i:])
    # print(set(list(s[:i])), set(list(s[i:])))
    # print(len(set(list(s[:i])) & set(list(s[i:]))))
    max_size = max(max_size, len(set(list(s[:i])) & set(list(s[i:]))))

print(max_size)