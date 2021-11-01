n = int(input())
s = input()

current = "a"
cnt_char = [0 for i in range(7)]
ans = 0
mod = pow(10, 9) + 7
for i in range(n):
    print("i", i, "current", current, s[i], ans)
    if current == "a":
        if s[i] == "a":
            cnt_char[0] += 1
        elif s[i] == "t":
            current = "t"
            cnt_char[1] += 1
        continue

    if current == "t":
        if s[i] == "t":
            cnt_char[1] += 1
        elif s[i] == "c":
            current = "c"
            cnt_char[2] += 1
        continue
    if current == "c":
        if s[i] == "c":
            cnt_char[2] += 1
        elif s[i] == "o":
            current = "o"
            cnt_char[3] += 1
        continue
    if current == "o":
        if s[i] == "o":
            cnt_char[3] += 1
        elif s[i] == "d":
            current = "d"
            cnt_char[4] += 1
        continue
    if current == "d":
        if s[i] == "d":
            cnt_char[4] += 1
        elif s[i] == "e":
            current = "e"
            cnt_char[5] += 1
        continue
    if current == "e":
        if s[i] == "e":
            cnt_char[5] += 1
        elif s[i] == "r":
            current = "r"
            cnt_char[6] += 1
        continue
    if current == "r":
        if s[i] == "r":
            cnt_char[6] += 1
        elif s[i] == "a":
            ans += (
                cnt_char[0]
                * cnt_char[1]
                * cnt_char[2]
                * cnt_char[3]
                * cnt_char[4]
                * cnt_char[5]
                * cnt_char[6]
            )
            ans %= mod
            cnt_char = [0 for i in range(7)]
            current = "a"
            cnt_char[0] += 1
        continue

print(cnt_char)
ans += (
    cnt_char[0]
    * cnt_char[1]
    * cnt_char[2]
    * cnt_char[3]
    * cnt_char[4]
    * cnt_char[5]
    * cnt_char[6]
)
ans %= mod
print(ans)