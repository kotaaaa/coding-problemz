n = int(input())
c = [0 for _ in range(n-1)]
s = [0 for _ in range(n)]
f = [0 for _ in range(n-1)]
for i in range(n-1):
    c[i],s[i],f[i] = map(int,input().split())

def solve(fr):
    wait_times = [0 for _ in range(n)]
    wait_at_station = [0 for _ in range(n)]
    # any_wait_at_station = [0 for _ in range(n)]
    times = [0 for _ in range(n)]
    all_time = 0
    wait = 0
    for i in range(fr, n-1):
        if all_time < s[i]:
            all_time = s[i]
            wait_at_station[i] = 1
        else:
            if all_time % f[i] == 0:
                wait = 0
            else:
                wait = f[i] - (all_time % f[i])
            wait_times[i] = wait
            all_time += wait_times[i]
        all_time += c[i]
    print(all_time)

for station in range(n-1):
    solve(station)
print(0)

# times[0] = all_time
# for i in range(1,n):
#     if wait_at_station[i] == 0:
#         all_time = all_time - c[i-1] - s[i-1] + s[i] - wait_times[i]
#     times[i] = all_time

# print(wait_at_station)
# for i in range(n):
#     print(times[i])
