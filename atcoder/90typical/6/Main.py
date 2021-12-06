n,k = map(int,input().split())
s = input()

# print(sorted(s[:9]))
# print(sorted(s[:10]))
# print(sorted(s[:11]))
# print(sorted(s[:12]))
# print(sorted(s[:13]))
# print(sorted(s))

# ans = sorted(s[:n-k+1])[0]
x = 'z'
idx = n
print(s[:n-k+1])
for i_ in range(len(s[:n-k+1])):
    if s[:n-k+1][i_] < x:
        x = s[:n-k+1][i_]
        idx = i_
ans = s[idx]
limit = n-k+1
i = idx
# ans = ""
print("ans ss",ans)
while len(ans) < k:
    print("i",i,"s[i]",s[i],"ans",ans)
    if s[idx] < s[i]:
        idx = i
        ans += s[i]
    if i == limit:
        ans += s[i:]
        break
    i += 1
print(ans)