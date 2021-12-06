x,y = map(int, input().split())

def cal (x_,y_):
    cnt = 0
    if x_ < 0:
        cnt += 1
    if y_ < 0:
        cnt += 1
    cnt += abs(abs(x_) - abs(y_))
    return cnt

if x >= 0 and y >= 0 and x > y:
    if x == 0 or y == 0:
        print(x-y+1)
    else:
        print(x-y+2)
    exit()

if x < y and abs(x) > abs(y) and x < 0 and y < 0:
    print(y-x)
    exit()

if x < y:
    print(min(cal(x,y),y-x))
    exit()


print(cal(x,y))
