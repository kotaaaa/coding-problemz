import copy

n = int(input())
h = list(map(int, input().split()))


sum_h = copy.copy(h)
cnt = 0 
all_zero = False

while not all_zero:
    all_zero = True
    before_0 = True
    for i in range(n):

        if sum_h[i] > 0:

            if before_0:
                cnt += 1

            all_zero = False
            before_0 = False
            sum_h[i] -= 1
        else:
            before_0 = True
    # print(sum_h,cnt)
print(cnt)