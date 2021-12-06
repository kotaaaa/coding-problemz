s = input()

set_s = set(list(s))
# print(set_s)

if len(set_s) == 1:
    print(0)
    exit()

import copy

min_all_same = 101

for i in set_s:
    # part_s = copy.copy(s)
    # if not i == 's':
        # continue
    part_s = list(s)
    len_s = len(s)
    while len_s > 0:
        
        all_same = True
        for j in range(len_s-1):
            # part_s = part_s[:len_s]
            # print(i, part_s, len_s, j,min_all_same)
            
            if part_s[j] == i or part_s[j+1] == i:
                part_s[j] = i
            else:
                # all_same = False
                # part_s[j] = i
                pass
        part_s = part_s[:len_s-1]
        # if all_same:
        #     print(len(s),len_s-1)
        #     min_all_same = min(min_all_same, len(s)-len_s+1)
        #     # print(len(s)-len_s)
        #     # exit()
        #     break
        for j in range(len(part_s)-1):
            if not part_s[j] == part_s[j+1]:
                all_same = False
                break
        if all_same:
            min_all_same = min(min_all_same, len(s)-len(part_s))
        len_s -= 1
    # break
print(min_all_same)



