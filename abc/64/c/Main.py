n = int(input())
a = list(map(int, input().split()))

colores = [0 for _ in range(9)]
for i in a:
    if i >= 3200:
        colores[8] += 1
        continue
    
    colores[i // 400] += 1

# print(colores)

min_cnt = 0
# max_cnt = 0
for i in colores[:8]:
    if i >= 1:
        min_cnt += 1

print(max(min_cnt,1),min_cnt+colores[8])
