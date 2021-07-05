s = input()

bool_0 = True
# cnt = 0
for i in range(len(s)//2):
    # print("a",s_no_x[i])
    if s[i] != s[len(s)-1-i]:
        bool_0 = False
        break
    # else:
        # cnt += 2
    # elif s_no_x[i] == "x":
        # x_cnt -= 2
if bool_0:
    # if len(s) % 2 == 1:
        # cnt += 1
    print(0)
    exit()

s_no_x_list = []
x_cnt = 0
for i in s:
    if i != "x":
        s_no_x_list.append(i)
    else:
        x_cnt += 1
s_no_x = "".join(s_no_x_list)
for i in range(len(s_no_x)//2):
    # print("a",s_no_x[i])
    if s_no_x[i] != s_no_x[len(s_no_x)-1-i]:
        print(-1)
        exit()

idx = 0
# for i in range(len(s)):
#     if idx == len(s_no_x)//2:
#        s[i] == "x"
#     elif idx > len(s_no_x)//2:
#         break

#     if s[i] != "x":
#         idx += 1

print(x_cnt)
