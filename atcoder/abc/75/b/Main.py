h,w = map(int, input().split())
mass = [[] for _ in range(h)]
for i in range(h):
    mass[i] =  list(input())

# print(mass)

bombs = []
for i in range(h):
    for j in range(w):
        if mass[i][j] == '#':
            bombs.append((i,j))

direction = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
nums = [[0 for _ in range(w)] for _ in range(h)]
for b_y, b_x in bombs:
    for y_, x_ in direction:
        if b_y + y_ < 0 or b_y + y_ >= h or b_x + x_ < 0 or b_x + x_ >= w or mass[b_y + y_][b_x + x_] == '#':
            continue
        nums[b_y + y_][b_x + x_] += 1

# print(nums)
for i in range(h):
    for j in range(w):
        if mass[i][j] == '#':
            print('#', end='')
        else:
            print(nums[i][j], end='')
    print()