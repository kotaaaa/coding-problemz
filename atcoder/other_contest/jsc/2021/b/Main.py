n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_b = set(a) & set(b)
# print(a_b)

ans = []
for i in a:
    if not i in a_b:
        ans.append(i)

for i in b:
    if not i in a_b:
        ans.append(i)
ans.sort()
for i in ans:
    print(i,end=" ")