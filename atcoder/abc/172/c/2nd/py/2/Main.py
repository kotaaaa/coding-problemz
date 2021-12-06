import math
import sys



n,m,k = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# ここから
# f = open("b9in.txt")  #19: 200000, 9: 113897
# l = f.readlines()
# n,m,k = map(int,l[0].split())
# a = [0] + list(map(int, l[1].split()))
# b = [0] + list(map(int, l[2].split()))
#  # ここまで

sum_a = [0 for i in range(n+1)]
sum_b = [0 for i in range(m+1)]

sum_a[0] = 0 # a[0]
for i in range(n):
    sum_a[i+1] += sum_a[i] + a[i]

sum_b[0] = 0 #b[0]
for i in range(m):
    sum_b[i+1] += sum_b[i] + b[i]

# print(sum_a)
# print(sum_b)

max_books = 0
for i in range(n+1):
    target = k-sum_a[i]
    if target < 0:
        break
    left = 0
    right = m
    # print("max_books ", max_books, "target ",target) #, "sum_b[left] ",sum_b[left], "sum_b[right]", sum_b[right])
    # if target < sum_b[left]:
    #     max_books = max(max_books, (i + 1))
    #     continue
    # if target >= sum_b[right]:
    #     max_books = max(max_books, m + (i + 1))
        # continue

    while left + 1 < right:
        mid = (left + right) // 2
        if sum_b[mid] <= target:
            left = mid
        # elif sum_b[mid] == target:
            # left += 1
            # left = mid
            # break
        elif sum_b[mid] > target:
            right = mid

    # print(max_books, left-1, sum_b[left-1], right, mid)
    max_books = max(max_books, left + i)
    
print(max_books)


# 6 4 730
# 60 90 120 100 50 50
# 80 150 80 150