from collections import deque

k = int(input())

queue = deque()
for i in range(1, 10):
    queue.append(i)

cnt = 0
while queue:
    target = queue.popleft()
    cnt += 1
    # print(queue,target,cnt)
    if cnt == k:
        break
    if target % 10 - 1 >= 0 and target % 10 - 1 <= 9:
        queue.append(10 * target + target % 10 - 1)
    if target % 10 >= 0 and target % 10 <= 9:
        queue.append(10 * target + target % 10)
    if target % 10 + 1 >= 0 and target % 10 + 1 <= 9:
        queue.append(10 * target + target % 10 + 1)
print(target)