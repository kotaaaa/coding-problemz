s = input()
if s == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
# alpha2num = lambda c: ord(c) - ord('A') + 1
alphabet = [0 for i in range(26)]

kind_cnt = 0
alpha2num = lambda c: ord(c) - ord('a')

for i in s:
    # print("char_num(i)",alpha2num(i))
    alphabet[alpha2num(i)] += 1
    if alphabet[alpha2num(i)] == 1:
        kind_cnt += 1

# print(alphabet)
num2alpha = lambda c: chr(c+97)
if kind_cnt == 26:
    # print(s)
    # for i in range(26):
        # print(alpha2num(s[i]))    
    for i in range(25,0,-1):
        # print(alpha2num(s[i]))
        # print(alpha2num(s[i]),alpha2num(s[i-1]))
        # print(s[i],s[i-1])
        # print(alpha2num(s[i]),alpha2num(s[i-1]))
        if alpha2num(s[i]) < alpha2num(s[i-1]):
            # print(s[i],s[i-1])
            continue
        else:
            # print("s[:i-2]",s[:i-2],s[i],s[i-1])
            # print(s[:i-1]+num2alpha(alpha2num(s[i-1])+1)) # // (s[i])+(s[i-1]))
            # print(s[:i-1]+s[-1])
            tmp = sorted(s[i:])
            # print(tmp)
            for j in tmp:
                if s[i-1] < j:
                    print(s[:i-1]+j)
                    exit()
            
            exit()
    #     # print(si)
    #     if s[i] == num2alpha(i):
    #         continue
        # else:
            # s[s[:i-2]]+
else:
    for i in range(26):
        if alphabet[i] == 0:
            print(s+num2alpha(i))
            exit()
# zyxwvutsrqponmlkjihgfedcba