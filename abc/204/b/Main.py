n = int(input())
a = list(map(int, input().split()))

val = 0
for i in a:
    if i <= 10:
        continue
    val += (i-10)
print(val)