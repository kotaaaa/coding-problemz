
h,w,y,x = map(int, input().split())

mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

ans = 1 
# right 
y_ = y-1
x_ = x-1
while True:
    x_ += 1
    if x_ < 0 or x_ >= w: 
        break
    # print(y_, x_)
    if mass[y_][x_] == '#':
        break
    ans += 1
    
# print(ans)
# left
y_ = y-1
x_ = x-1
while True:
    x_ -= 1
    if x_ < 0 or x_ >= w: 
        break
    if mass[y_][x_] == '#':
        break
    ans += 1
    
# print(ans)
# up 
y_ = y-1
x_ = x-1
while True:
    y_ += 1
    if y_ < 0 or y_ >= h: 
        break
    if mass[y_][x_] == '#':
        break
    ans += 1
    

# print(ans)
# down 
y_ = y-1
x_ = x-1
while True:
    y_ -= 1
    if y_ < 0 or y_ >= h: 
        break
    if mass[y_][x_] == '#':
        break
    ans += 1



print(ans)