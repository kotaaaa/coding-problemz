n = int(input())
s =  list(input())

right_east = 0
right_west = 0
left_east = 0
left_west = 0

for i in range(n):
    if s[i] == 'E':
        right_east += 1
    if s[i] == 'W':
        right_west += 1
    
min_count = 300001
for i in range(n):
    if s[i] == 'E':
        right_east -= 1
    if s[i] == 'W':
        right_west -= 1

    min_count = min(min_count, left_west+right_east)

    if s[i] == 'E':
        left_east += 1
    if s[i] == 'W':
        left_west += 1
print(min_count)