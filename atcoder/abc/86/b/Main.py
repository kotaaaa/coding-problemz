n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())


current = (0,0)
current_time = 0
for i in range(n):
    man_distance = abs(x[i] - current[0]) + abs(y[i] - current[1])
    time_diff = t[i] - current_time
    # print(man_distance, time_diff)
    if man_distance > time_diff or man_distance % 2 != time_diff % 2:
        print("No")
        exit()
    current = (x[i],y[i])
    current_time = t[i]


print("Yes")