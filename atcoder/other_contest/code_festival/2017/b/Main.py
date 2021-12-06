n = int(input())
d = list(map(int, input().split()))

m = int(input())
t = list(map(int, input().split()))

candidates = {}
problems = {}

for i in d:
    if i in candidates:
        candidates[i] += 1
    else:
        candidates[i] = 1

for i in t:
    if i in problems:
        problems[i] += 1
    else:
        problems[i] = 1

# print(candidates)
# print(problems)

for k,v in problems.items():
    if not k in candidates:
        print("NO")
        exit()
    if candidates[k] < v:
        print("NO")
        exit()

print("YES")