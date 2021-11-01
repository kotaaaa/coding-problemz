from collections import deque

x, y = map(int, input().split())

queue = deque()
queue.append([0, 0])

visited = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
visited[0][0] = 0
while len(queue) > 0:
    target = queue.pop()
    # x - target[0]
    # y - target[1]

    if target[0] + 2 > x or target[1] + 1:
    # if y >= target[1] + 2*(x - target[0]):

    # if 
    # min_xy = min(x - target[0], y - target[1])
    # max_xy = max(x - target[0], y - target[1])
    # if target[0] + 2 * min_xy > target[1] * max_xy:
    #     queue.append([target[0] + 1, target[1] + 2])
    #     visited[target[0] + 1, target[1] + 2] = 1
    # if target[1] + 2 * min_xy > target[0] * max_xy:
    #     queue.append([target[0] + 2, target[1] + 1])
    #     visited[target[0] + 2, target[1] + 1] = 1
    
