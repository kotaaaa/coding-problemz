n,k = map(int,input().split())
a = list(map(int,input().split()))

amari = k % n 
syo = k // n
syos = [syo for _ in range(n)]
sorted_a = [i[0] for i in sorted(enumerate(a), key=lambda x:x[1], reverse=False)]
# print(sorted_a)

for i in range(amari):
    # print(sorted[i])
    # print(syos[sorted[i]])
    syos[sorted_a[i]] += 1
for i in range(n):
    print(syos[i])

    




