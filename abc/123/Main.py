import math 

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a_cnt = 0
b_cnt = 0
c_cnt = 0
d_cnt = 0
e_cnt = 0

a_cnt = math.ceil(n / a)
b_min = min(a,b)
b_cnt = math.ceil(n / b_min)
c_min = min(b_min,c)
c_cnt = math.ceil(n / c_min)
d_min = min(c_min,d)
d_cnt = math.ceil(n / d_min)
e_min = min(d_min,e)
e_cnt = math.ceil(n / e_min)

# print("cnt")
# print(a_cnt)
# print(b_cnt)
# print(c_cnt)
# print(d_cnt)
# print(e_cnt)

ans = a_cnt
ans += (b_cnt - a_cnt) + 1
ans += (c_cnt - b_cnt) + 1
ans += (d_cnt - c_cnt) + 1
ans += (e_cnt - d_cnt) + 1

print(ans)