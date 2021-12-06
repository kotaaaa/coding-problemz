n = int(input())
a = list(map(int, input().split()))

arr = [0 for i in range(n)]
for i in a:
    arr[i-1] += 1

for i in range(n):
    if arr[i] != 1:
        print("No")
        exit()
print("Yes")    
