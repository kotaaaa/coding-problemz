s = int(input())
a = list(map(int, input().split()))

cnts = [0 for i in range(401)]
for i in a:
    cnts[i+200] += 1

# print(cnts)
ans = 0
for i in range(-200,201):
    for j in range(i+1,201):
        # print(i,j)
        # ans += abs(i*j)*cnts[i+200]*cnts[j+200]
        ans += (i-j)**2*cnts[i+200]*cnts[j+200]

print(ans)