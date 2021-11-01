n = int(input())
v = list(map(int,input().split()))

odds = {}
evens = {}

a = v[0]
all_same = True
for i in range(n):
    if a != v[i]:
        all_same = False
        break

if all_same:
    print(n//2)
    exit()

for i in range(n):
    if i % 2 == 0:
        if v[i] in evens:
            evens[v[i]] += 1
        else:
            evens[v[i]] = 1
    else:
        if v[i] in odds:
            odds[v[i]] += 1
        else:
            odds[v[i]] = 1

# sorted_evens = sorted(range(len(evens)), key=lambda k: k[0], reverse=True)
# sorted_odds = sorted(range(len(odds)), key=lambda k: k[0], reverse=True)
sorted_evens = sorted(evens.items(), key=lambda i: i[1],reverse=True)
sorted_odds = sorted(odds.items(), key=lambda i: i[1],reverse=True)
# print(sorted_evens)
# print(sorted_odds)

if sorted_evens[0][0] != sorted_odds[0][0]:
    print(n - sorted_evens[0][1] - sorted_odds[0][1])
else:
    if len(sorted_evens) == 1:
        print(n - sorted_evens[0][1] - sorted_odds[1][1])
        exit()
    if len(sorted_odds) == 1:
        print(n - sorted_evens[1][1] - sorted_odds[0][1])
        exit()

    if sorted_evens[1][1] < sorted_odds[1][1]:
        print(n - sorted_evens[0][1] - sorted_odds[1][1])
    else:
        print(n - sorted_evens[1][1] - sorted_odds[0][1])
