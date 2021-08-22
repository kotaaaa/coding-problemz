n = int(input())
a = list(map(int, input().split()))

# 不明: 0, +:1, - :-1
direction = 0 
before = a[0]
divide_cnt = 0
for i in a[1:]:
    if direction == 0:
        if before < i:
            direction = 1
        elif before == i:
            pass
        else:
            direction = -1

    elif direction == 1:
        if before < i:
            pass
        elif before == i:
            pass
        else:
            direction = 0
            divide_cnt += 1

    elif direction == -1:
        if before < i:
            direction = 0
            divide_cnt += 1
        elif before == i:
            pass
        else:
            pass
        
    # print(i, divide_cnt,direction)
    before = i
        
print(divide_cnt+1)
    

