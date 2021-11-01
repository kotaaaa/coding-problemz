s = input()
k = int(input())

if len(s) == 1:
    print(k // 2)
    exit()

before = s[0]
cnt = 1
delete_cnt = 0

for i in range(1,len(s)):
    # print(before, s[i])
    if before == s[i]:
        cnt += 1
        if cnt % 2 == 0:
            delete_cnt += 1
    else:
        before = s[i]
        cnt = 1

# print(delete_cnt)

left_cnt = 1
right_cnt = 1
left_char = s[0]
right_char = s[len(s)-1]

for i in range(1,len(s)):
    if s[i] == left_char:
        left_cnt += 1
    else:
        break

for i in range(len(s)-2,-1,-1):
    if s[i] == right_char:
        right_cnt += 1
    else:
        break

if right_cnt == left_cnt and right_cnt == len(s):
    print(len(s)*k // 2)
    exit()    

# print("l ",left_cnt,"r ",right_cnt)
if left_char == right_char and left_cnt % 2 == 1 and right_cnt % 2 == 1:
    print(delete_cnt*k+(k-1))
else:
    print(delete_cnt*k)
