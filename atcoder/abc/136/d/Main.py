s = input()
cnt = [0 for i in range(len(s))]
r_cnt = 0
l_cnt = 0

checked = [False for i in range(len(s))]

for i in range(len(s)-1,-1,-1):
    if s[i] == 'R':
        r_cnt += 1
    else:
        r_cnt = 0
    
    if r_cnt >= 4:
        if r_cnt % 2 == 0:
            cnt[i + r_cnt] += 1
        else:
            cnt[i + r_cnt - 1] += 1
        checked[i] = True
        continue

for i in range(len(s)):
    if s[i] == 'R':
        if checked[i]:
            continue
        # r_cnt += 1
        l_cnt = 0
        # if r_cnt >= 4:
        #     if r_cnt % 2 == 0:
        #         s[i + r_cnt] += 1
        #     else:
        #         s[i + r_cnt - 1] += 1
        #     continue

        if s[i+1] == 'R':
            cnt[i+2] += 1
        else:
            cnt[i] += 1
    else:
        r_cnt = 0
        l_cnt += 1
        # print(l_cnt)
        if l_cnt >= 4:
            if l_cnt % 2 == 0:
                cnt[i - l_cnt] += 1
            else:
                cnt[i - l_cnt + 1] += 1
            # print(cnt)
            continue
        if s[i-1] == 'L':
            cnt[i-2] += 1
        else:
            cnt[i] += 1
    # print(cnt)

for i in range(len(s)):
    print(cnt[i],end=" ")
