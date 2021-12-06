n,a,b,c,d = map(int, input().split())
s = input()

end = max(c,d)
for i in range(a,end-2):
    if s[i] == '#' and s[i+1] == '#':
        print("No")
        exit()
    
if c < d:
    print("Yes")
    exit()

for i in range(b-1, d):
    if s[i-1] == '.' and s[i] == '.' and s[i+1] == '.':
        print("Yes")
        exit()

print("No")
    
