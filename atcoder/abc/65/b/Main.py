n = int(input())
a = [0 for i in range(n+1)]
for i in range(1,n+1):
    a[i] = int(input())


visited = [0 for i in range(n+1)]
current = 1
visited[1] = 1
cnt = 0
while True:
    current = a[current]
    cnt += 1
    if current == 2:
        print(cnt)
        exit()
    if visited[current] == 1:
        print("-1")
        exit()
    visited[current] = 1