n = int(input())
s = input()

mod = pow(10,9)+7

char_dict = {}
for i in s:
    if i in char_dict:
        char_dict[i] += 1
    else:
        char_dict[i] = 1

ans = 1
for k in char_dict.keys():
    ans *= char_dict[k]+1
    ans %= mod 

print(ans-1)

