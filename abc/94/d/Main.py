n = int(input())
a = list(map(int, input().split()))
a.sort()

amax = a.pop()
# print(a)
# print(amax)
# print(a[0],a[0]//2)

minj = pow(10,9)+1
j = pow(10,9)+1
for i in a:
    # minj = min(minj,abs(i - amax//2))
    if minj > abs(i - amax/2):
        minj = abs(i - amax/2)
        j = i
print(amax,j)