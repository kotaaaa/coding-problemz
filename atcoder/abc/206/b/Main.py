n = int(input())

i = 1
while True:
    if (i*(i+1))//2 >= n:
        print(i)
        break
    i += 1
