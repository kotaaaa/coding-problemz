sd = input()
t = input()

ns = len(sd)
nt = len(t)

candidates = []
for i in range(ns - nt + 1):
    # print(sd[i:i+nt])
    is_possible = True
    for j,c in enumerate(sd[i:i+nt]):
        # print(t[j],c)
        if t[j] != c and c != "?":
            is_possible = False
            break
    if is_possible:
        # candidates.append(sd[i:i+nt]) 
        candidates.append(i) 

if len(candidates) == 0:
    print("UNRESTORABLE")
    exit()
# print(sd[:i],"@",t,"@",sd[i+nt:])
i = candidates.pop()
ans = sd[:i]+t+sd[i+nt:]
# print(sd[:i]+t+sd[i+nt:])
ans = ans.replace("?", "a")
print(ans)
# print(candidates)
    