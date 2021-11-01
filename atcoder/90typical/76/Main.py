n = int(input())
a = list(map(int,input().split()))

sum_val = 0
for i in range(n):
    sum_val += a[i]

if sum_val % 10 != 0:
    print("No")
    exit()

left = 0
right = 1


# print(a)
piece = a[0]
a = a + a #[piece]
# print(a)
target = sum_val // 10
while True:
    if left >= 2*n and right >= 2*n:
        break
    # print("left right",left,right,piece,target)
    if piece == target:
        print("Yes")
        exit()
    elif right < 2*n and piece < target:
        piece += a[right]
        right += 1
    else:
        piece -= a[left]
        left += 1
print("No")