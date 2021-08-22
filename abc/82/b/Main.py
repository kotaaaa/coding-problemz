s = input()
t = input()

sort_s = sorted(s)
sort_t = sorted(t, reverse = True)

sort_s = ''.join(sort_s)
sort_t = ''.join(sort_t)
# print(sort_s,sort_t)

if sort_s < sort_t:
    print("Yes")
else:
    print("No")