n = int(input())
s = input()
q = int(input())

t = [0] * q
a = [0] * q
b = [0] * q
for i in range(q):
    t[i], a[i], b[i] = map(int, input().split())

for i in range(q):
    if t[i] == 1:
        tmp_a = s[a[i] - 1]
        tmp_b = s[b[i] - 1]
        # print(tmp_a, tmp_b)
        # print(s[: a[i] - 1], tmp_b , s[a[i] : b[i] - 1] , tmp_a , s[b[i] :])
        # tmp_s.append(s[: a[i] - 1])
        # tmp_s.append(tmp_b)
        # tmp_s.append(s[a[i] : b[i] - 1])
        # tmp_s.append(tmp_a)
        # tmp_s.append(s[b[i] :])
        # s = s[: a[i] - 1] + tmp_b + s[a[i] : b[i] - 1] + tmp_a + s[b[i] :]
        # s = ''.join(tmp_s)
        s = '{}{}{}{}{}'.format(s[: a[i] - 1],tmp_b,s[a[i] : b[i] - 1],tmp_a,s[b[i] :])
    else:
        # print(s[n//2 - 1:])
        # s = s[n:] + s[: n]
        s = '{}{}'.format(s[n:],s[: n])
print(s)
