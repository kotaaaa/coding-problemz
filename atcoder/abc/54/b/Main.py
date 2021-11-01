n, m = map(int, input().split())

mass_a = [[] for _ in range(n)]
for i in range(n):
    mass_a[i] =  list(input())

mass_b = [[] for _ in range(m)]
for i in range(m):
    mass_b[i] =  list(input())
# print(mass_a)
# print(mass_b)
target_i = 0
target_j = 0

for i in range(n-m+1):
    for j in range(n-m+1):
        is_existed = True
        for mi in range(m):
            for mj in range(m):
                # print(mass_b[mi][mj])
                if mass_a[i+mi][j+mj] != mass_b[mi][mj]:
                    is_existed = False
                    break
        if is_existed:
            print("Yes")
            exit()

print("No")