sx,sy,tx,ty = map(int,input().split())

dx = tx - sx
dy = ty - sy

direction = ["U","R","D","L"]
current = 0 

# print("dx",dx,"dy",dy)
## 上から
if dx >= 0 and dy > 0:
    current = 0 
    for _ in range(dy):
        print("U",end="")
    for _ in range(max(1,dx)):
        print("R",end="")
    for _ in range(dy):
        print("D",end="")
    for _ in range(max(2,dx+1)):
        print("L",end="")
    for _ in range(1+dy):
        print("U",end="")
    for _ in range(max(2,dx+1)):
        print("R",end="")
    print("D",end="")
    print("R",end="")
    for _ in range(1+dy):
        print("D",end="")
    for _ in range(max(2,dx+1)):
        print("L",end="")
    print("U",end="")

## 右から
if dx > 0 and dy <= 0:
    current = 0 
    for _ in range(dy):
        print("R",end="")
    for _ in range(max(1,dx)):
        print("D",end="")
    for _ in range(dy):
        print("L",end="")
    for _ in range(max(2,dx+1)):
        print("U",end="")
    for _ in range(1+dy):
        print("R",end="")
    for _ in range(max(2,dx+1)):
        print("D",end="")
    print("L",end="")
    print("D",end="")
    for _ in range(1+dy):
        print("L",end="")
    for _ in range(max(2,dx+1)):
        print("U",end="")
    print("R",end="")

## 下から
if dx > 0 and dy <= 0:
    current = 0 
    for _ in range(dy):
        print("D",end="")
    for _ in range(max(1,dx)):
        print("L",end="")
    for _ in range(dy):
        print("U",end="")
    for _ in range(max(2,dx+1)):
        print("R",end="")
    for _ in range(1+dy):
        print("D",end="")
    for _ in range(max(2,dx+1)):
        print("L",end="")
    print("U",end="")
    print("L",end="")
    for _ in range(1+dy):
        print("U",end="")
    for _ in range(max(2,dx+1)):
        print("R",end="")
    print("D",end="")

## 左から
if dx > 0 and dy <= 0:
    current = 0 
    for _ in range(dy):
        print("L",end="")
    for _ in range(max(1,dx)):
        print("U",end="")
    for _ in range(dy):
        print("R",end="")
    for _ in range(max(2,dx+1)):
        print("D",end="")
    for _ in range(1+dy):
        print("L",end="")
    for _ in range(max(2,dx+1)):
        print("U",end="")
    print("R",end="")
    print("U",end="")
    for _ in range(1+dy):
        print("R",end="")
    for _ in range(max(2,dx+1)):
        print("D",end="")
    print("L",end="")


