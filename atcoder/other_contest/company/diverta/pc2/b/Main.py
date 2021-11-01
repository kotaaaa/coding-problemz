n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

def get_n(val):
    ans = 1
    while True:
        if (ans * (ans + 1))//2 == val:
            return ans
        ans += 1

# az = set()
az_dict = {}
none_cnt = 0
cnt_0 = 0
for i in range(n):
    for j in range(i+1,n):
        if x[j] - x[i] == 0:
            # az.add((None,x[i]))
            none_cnt += 1
            continue
        if y[j] - y[i] == 0:
            # az.add((None,x[i]))
            cnt_0 += 1
            continue
        a = (y[j]-y[i])/(x[j]-x[i])
        if a in az_dict:
            az_dict[a] += 1
        else:
            az_dict[a] = 1
max_val = 0 
if none_cnt > 0:
    # max_val = max(n-none_cnt,n-cnt_0)+1
    max_val = n-none_cnt + 1
if cnt_0 > 0:
    max_val = max(n-cnt_0 + 1,max_val)
# print(max_val)
# print(az_dict,none_cnt)
for i in az_dict:
    max_val = max(max_val,az_dict[i])
# print("max_val",max_val)
print(n-get_n(max_val))
        # az.add((a,y[j]-a*x[i])

# max_cnt = 0
# for i in az:
#     cnt = 0
#     if i[0] == None:
#         for j in range(n):
#             if i[1] == x[j]:
#                 cnt += 1
#         max_cnt = max(max_cnt,cnt)
#         continue
    
#     for j in range(n):
#         if i[0]*x[j] + i[1] == y[j]:
#             cnt += 1
#     max_cnt = max(max_cnt,cnt)
#     print("傾き",i,max_cnt,cnt)
# print(n-max_cnt+1)
