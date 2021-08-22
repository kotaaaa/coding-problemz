n = int(input())

n_str = str(n)

if n < 10:
    print(0)
    exit()
if len(n_str) % 2 == 1:
    ans = str(10**(len(n_str)-1)-1)
    print(ans[:(len(n_str)-1)//2])
    exit()

left = int(n_str[:(len(n_str)//2)])
right = int(n_str[(len(n_str)//2):])
# print(left, right)

# if right < 10**(len(n_str)//2-1):
#     # print("a")
#     print(10**(len(n_str)//2-1)-1)
#     exit()
if left <= right:
    print(left)
else:
    # print(right)
    print(left-1)