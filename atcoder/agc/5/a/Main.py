x = input()

s_cnt = 0
t_cnt = 0

rest_cnt = 0
for i in x:
    # print(s_cnt,t_cnt,rest_cnt)
    if i == "T":
        if s_cnt <= t_cnt:
            rest_cnt += 1
        else:
            t_cnt += 1
            rest_cnt -= 1
    else:
        s_cnt += 1
        rest_cnt += 1
print(rest_cnt)

            