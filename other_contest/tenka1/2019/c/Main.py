n = int(input())
s = input()

dot_no_cnt = 0
sharp_no_cnt = 0
dot_cnt = 0
sharp_cnt = 0

for i in range(n):
    if s[i] == ".":
        dot_cnt += 1
    # else:
        # sharp_cnt += 1

ans = dot_cnt

for i in range(n):
    if s[i] == ".":
        dot_cnt -= 1
    else:
        sharp_cnt += 1
    ans = min(ans,dot_cnt+sharp_cnt)
print(ans)


# for i in range(n):
#     if s[i] == ".":
#         dot_no_cnt += 1
#     else:
#         break

# for i in range(n-1,-1,-1):
#     if s[i] == "#":
#         sharp_no_cnt += 1
#     else:
#         break
    
# if dot_no_cnt + sharp_no_cnt == n:
#     print(0)
#     exit()

# # print(dot_cnt,sharp_cnt,dot_no_cnt,sharp_no_cnt)
# print(min(dot_cnt-dot_no_cnt,sharp_cnt-sharp_no_cnt))