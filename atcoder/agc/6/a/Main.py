n = int(input())
s = input()
t = input()

for i in range(n,0,-1):
    # print(i,s[-1*i:])
    # t[]
    # print(t[:i])
    if s[-1*i:] == t[:i]:
        print(len(s+t[i:]))
        exit()
print(len(s+t))