n = int(input())
s = [input() for i in range(n)]

map_list = []
alfa = set()

for i in range(n):
    char_map = {}
    for j in range(len(s[i])):
        if s[i][j] in char_map:
            char_map[s[i][j]] += 1
        else:
            char_map[s[i][j]] = 1
        
        alfa.add(s[i][j])

    map_list.append(char_map)

s = ''

for i in alfa:
    min_num = 51
    for j in range(n):
        if i in map_list[j]:
            min_num = min(min_num, map_list[j][i])
        else:
            min_num = 0
    s += i*min_num

print(''.join(sorted(s)))

    
