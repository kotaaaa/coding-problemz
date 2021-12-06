import math
s = input()

for i in range((len(s)//2)-1):
    # print(s[0:i+1], s[i+1:2*(i+1)])
    if s[0:i+1] == s[i+1:2*(i+1)]:
        # print(2*(i+1))
        ans = 2*(i+1)
        # break
        continue
print(ans)

# print(len("wertyuiopasdfghjklzxcvbnmqqwertyuiopasdfghjklzxcv4wertyuiopasdfghjklzxcvbnmqqwertyuiopasdfghjklzxcvwertyuiopasdfghjklzxcvbnmqqwertyuiopasdfghjklzxcv4wertyuiopasdfghjklzxcvbnmqqwertyuiopasdfghjklzxcv"))

# qwertyuiopasdfghjklzxcvbnmqqwertyuiopasdfghjklzxcvbnm