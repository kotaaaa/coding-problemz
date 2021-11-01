s = input()

black_cnt = 0 
white_cnt = 0 
for i in range(len(s)):
    if s[i] == 'B':
        black_cnt += 1
    else: 
        white_cnt += 1

# print(black_cnt, white_cnt)

tmp_black_cnt = 0 
black_point = 0
for i in range(white_cnt):
    if s[i] == 'B':
        tmp_black_cnt += 1
    black_point += tmp_black_cnt

tmp_white_cnt = 0 
white_point = 0
for i in range(black_cnt-1):
    if s[-1*i-1] == 'W':
        tmp_white_cnt += 1
    white_point += tmp_white_cnt

# print("black_point",black_point)
# print("white_point",white_point)
print(black_point+white_point)


# BWBWBW
# WBBWBW
# WBWBBW
# WWBBBW