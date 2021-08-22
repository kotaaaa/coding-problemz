n = int(input())
s = input()

mod = 998244353
dp = [0 for _ in range(n)]
dp[0] = 1
# cnts = [0 for _ in range(10)]
# cnts[ord(s[0])-65] += 1
set_content = set()
before = s[0]
renzoku = 1
for i in range(1,n):

    # cnts[ord(s[i])-65] += 1
    # dp[i] = 2*dp[i-1] - (2**(cnts[ord(s[i])-65]-1))
    
    # if before == s[i]:
        # renzoku += 1
    # else:
    renzoku = 1
    if s[i] in set_content:
        for j in range(1,i+1):
            if s[i] != s[i-j]:
                renzoku += 1
            else:
                break
        dp[i] = dp[i-1]*2 - (i-renzoku)
    else:
        # dp[i] = dp[i-1] + 2*i
        dp[i] = dp[i-1]*2
    dp[i] %= mod
    set_content.add(s[i])
    before = s[i]
    # if s[i] == s[i-1]:
        # dp[i] = 2*dp[i-1]
    # else:
        # dp[i] = dp[i-1]
print(dp[n-1])
# print(cnts)
print(dp)