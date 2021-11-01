n = int(input())
s = [input() for _ in range(n)]

pair = [(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(0,3,4),(1,2,3),(1,2,4),(1,3,4),(2,3,4)]

march = [0 for _ in range(5)]

for i in range(n):
    if s[i][0] == 'M':
        march[0] += 1

    if s[i][0] == 'A':
        march[1] += 1

    if s[i][0] == 'R':
        march[2] += 1

    if s[i][0] == 'C':
        march[3] += 1

    if s[i][0] == 'H':
        march[4] += 1

res = 0 
for i in pair:
    res += march[i[0]]*march[i[1]]*march[i[2]]

print(res)