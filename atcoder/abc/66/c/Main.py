n = int(input())
a = list(map(int, input().split()))

# arr = []
# arr_append = arr.append

# for i in range(n):
#     if i % 2 == 0:
#         arr.insert(0,a[i])
#     else:
#         # arr.append(a[i])
#         arr_append(a[i])

even = [a[i] for i in range(n) if i % 2 == 0]
odd = [a[i] for i in range(n) if not i % 2 == 0]
even.reverse()
arr = even + odd

if n % 2 == 0:
    for i in range(n-1,-1,-1):
        print(arr[i],end=" ")
else:
    for i in range(n):
        print(arr[i],end=" ")
