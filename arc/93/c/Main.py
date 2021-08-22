n = int(input())
a = list(map(int, input().split()))


current = 0
all_cost = 0
for i in range(n):
    if i == 0:
        current = 0
    else:
        current = a[i-1]
    all_cost += abs(a[i] - current)

all_cost += abs(a[n-1])
# print(all_cost)

current = 0
next_ = 0
for i in range(n):
    if i == 0:
        current = 0
    else:
        current = a[i-1]
    if i == n-1:
        next_ = 0
    else:
        next_ = a[i+1]

    if current <= a[i] and a[i] <= next_:
        print(all_cost)
        continue
    if next_ <= a[i] and a[i] <= current:
        print(all_cost)
        continue
    if current <= next_ and next_ < a[i]:
        print(all_cost - abs(a[i]-next_)*2)
        continue
    if current <= next_ and a[i] < current:
        print(all_cost - abs(a[i]-current)*2)
        continue
    if next_ < current and current < a[i]:
        print(all_cost - abs(a[i]-current)*2)
        continue
    if next_ < current and a[i] < next_:
        print(all_cost - abs(a[i]-next_)*2)
        continue
