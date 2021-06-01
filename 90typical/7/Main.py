n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [int(input()) for _ in range(q)]
a.sort()
# print(a)
diff = [0 for i in range(n)]
for i in range(n - 1):
    diff[i+1] = (a[i + 1] + a[i]) / 2
# print(diff)

def solve(mid, val):
    if val >= diff[mid]:
        return True
    else:
        False

for query in b:
    right = n
    left = 0
    while right - left > 1:
        mid = (right + left) // 2
        if solve(mid, query):
            left = mid
        else:
            right = mid
    print(abs(query - a[left]))