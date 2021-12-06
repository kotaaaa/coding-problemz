n,c,k = map(int, input().split())
t = [int(input()) for i in range(n)]

buses = 0
time = 0
ppl = 0

t.sort()

# print(t)

for i in range(n):
    
    if i == n-1:
        buses += 1
        continue
    
    ppl +=1
    if ppl == 1:
        time = t[i]
    # print(ppl, t[i+1], time)
    if ppl >= c or t[i+1] - time > k:    
        ppl = 0
        buses += 1
    # else:
        # ppl +=1
    # print("buses",buses)
print(buses)