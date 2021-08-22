n = int(input())
s = input()

left_add_cnt = 0
right_add_cnt = 0
left_kakko_cnt = 0
right_kakko_cnt = 0
for i in range(n):
    if s[i] == "(":
        left_kakko_cnt += 1
    else:
        if left_kakko_cnt > 0:
            left_kakko_cnt -= 1
        else:        
            left_add_cnt += 1
    
for i in range(n-1,-1,-1):
    if s[i] == ")":
        right_kakko_cnt += 1
    else:
        if right_kakko_cnt > 0:
            right_kakko_cnt -= 1
        else:        
            right_add_cnt += 1
    
# print(left_add_cnt,right_add_cnt)
print(left_add_cnt*"("+s+right_add_cnt*")")
