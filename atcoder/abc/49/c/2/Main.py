s = input()

i = len(s)-1
is_ok = False
while True:
    # print("i",i,s[:i],s[i:],s[i-4:i])
    if i-4 >= 0 and s[i-4:i+1] == "dream":
        i -= 5
        if i == -1:
            is_ok = True
            break
    elif i-4 >= 0 and s[i-4:i+1] == "erase":
        i -= 5
        if i == -1:
            is_ok = True
            break
    elif i-5 >= 0 and s[i-5:i+1] == "eraser":
        i -= 6
        if i == -1:
            is_ok = True
            break
    elif i-6 >= 0 and s[i-6:i+1] == "dreamer":
        i -= 7
        if i == -1:
            is_ok = True
            break
    else:
        print("NO")
        exit()
print("YES")