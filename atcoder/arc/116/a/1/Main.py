
n = int(input())
a = [int(input()) for _ in range(n)]

for i in a:
    if i % 4 == 0:
        print("Even")
    elif i % 2 == 0:
        print("Same")
    else:
        print("Odd")
