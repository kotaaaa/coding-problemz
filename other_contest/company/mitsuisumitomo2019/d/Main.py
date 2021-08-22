n = int(input())
s = input()

cnt = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            # print(str(i)+str(j)+str(k),cnt)
            idx = 0
            existed = False
            for l in s:
                # print(l, str(i),idx)
                if idx == 0:
                    if str(i) == l:
                        idx += 1
                    continue
                if idx == 1:
                    if str(j) == l:
                        idx += 1
                    continue
                if idx == 2:
                    if str(k) == l:
                        existed = True
                        break
            if existed:
                cnt += 1
            # exit()
print(cnt)