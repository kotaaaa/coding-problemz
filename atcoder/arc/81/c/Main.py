n = int(input())
a = list(map(int, input().split()))

num_dict = {}
for i in a:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

sorted_nums = sorted(num_dict.items(), key=lambda x:x[0], reverse=True)
# print(sorted_nums)

time = 0
w = 0
h = 0

for k,v in sorted_nums: #.items():
    if time >= 2:
        break
    if v < 2:
        continue
    if time == 0:
        w = k
    else:
        h = k
    time += 1
    
time = 0
l = 0
for k,v in sorted_nums: #.items():
    if time >= 1:
        break
    if v < 4:
        continue
    l = k
    time += 1
    
# if w == 0 or h == 0:
#     print(0)
#     exit()
print(max(w*h,l*l))
