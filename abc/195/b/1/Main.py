import math
a,b,w = map(float, input().split())

w = w * 1000

min_val = 10**9
max_val = 0

# print(w / a)
# print(w / b)
# print(math.ceil(w/b))
# print(math.floor(w/a))
if math.ceil(w/b) > math.floor(w/a):
    print("UNSATISFIABLE")
    exit()
for i in range(int(math.ceil(w/b)), int(math.floor(w/a)+1)):
    # print(i)
    # if w % i == 0:
    min_val = min(min_val, i)
    max_val = max(max_val, i)

print(int(min_val),int(max_val))
# max_val = int(math.floor(w/a))
# min_val = int(math.ceil(w/b))
# print(int(min_val),int(max_val))