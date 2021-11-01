s = input()

i = 0
while i+7 < len(s):
    # print(s[i:i+5],(s[i:i+5] == "dream"),s[i+5:i+7])
    i_5 = s[i:i+5]
    i_56 = s[i+5:i+6]
    i5 = [i+5]
    if i_5 == "dream":
        if i_56 == "er":
            i+=7
            continue
        elif i5 == "d" or i5 == "e":
            i+=5
            # print(s[i:])
            continue
        else:
            print("NO")
            exit()
    if i_5 == "erase":
        if i5 == "r":
            print("a")
            i+=6
            continue
        elif i5 == "d" or i5 == "e":
            i+=5
            continue
        else:
            print("NO")
            exit()
    else:
        print("NO")
        # exit()
    # print("i",i)

if s[-7:] == "dreamer" or s[-6:] == "eraser" or s[-5:] == "dream" or s[-5:] == "erase":
    print("YES")
else:
    print("NO")
# print("7",s[-7:])
# print("6",s[-6:])
# print("5",s[-5:])
# if s[-7:-1]
# print("YES")