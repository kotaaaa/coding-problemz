n,k = map(int,input().split())

if n == 0:
    print(0)
    exit()

def base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = X_dumy//n
    return out

num = str(n)
for i in range(k):
    num = int(num,8)
    num = base_10_to_n(num,9)
    # print("1 ",num)
    num = str(num).replace("8","5")
    # print("2 ",num)
print(num)
