n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# fr = open("01.txt","r")

# e = fr.readlines()
# n = int(e[0])
# a = list(map(int, e[1].split()))
# b = list(map(int, e[2].split()))

plus = []
minus = []
for i in range(n):
    diff = a[i] - b[i]
    if diff > 0:
        plus.append(diff)
    elif diff < 0:
        minus.append(abs(diff))

plus.sort(reverse=True)
minus.sort(reverse=True)

# print(plus)
# print(minus)

plus_idx = 0
for i in minus:
    if plus[plus_idx] == 0:
        plus_idx += 1
    if plus[plus_idx] > i:
        plus[plus_idx] -= i
    elif plus[plus_idx] == i:
        plus[plus_idx] = 0
        # plus_idx += 1
    else:
        rest = i
        while True:
            
            if rest <= 0:
                break
            if plus[plus_idx] == 0:
                plus_idx += 1
                if plus_idx == len(plus):
                    print(-1)
                    exit()
            # print("rest", rest, "plus[plus_idx] ",plus[plus_idx])
            if plus[plus_idx] > rest:
                plus[plus_idx] -= rest
                rest = 0
                break
            elif plus[plus_idx] == i:
                plus[plus_idx] = 0
                rest = 0
                break
            else:
                rest = rest - plus[plus_idx]
                plus[plus_idx] = 0
                

# print(plus_idx, len(minus))

if len(minus) == 0:
    print(0)
else:
    print(len(minus)+plus_idx+1)

