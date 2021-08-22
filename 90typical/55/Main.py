import itertools

n,p,q = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
# for i in itertools.permutations(a,5):
for i in itertools.combinations(a,5):  
    val = 1
    # for j in i:
        # val *= (j % p)
    if i[0] % p * i[1] % p * i[2] % p * i[3] % p * i[4] % p == q:
    # print(i,val,(val % p == q),val % p,cnt)
    # if val % p == q:
        cnt += 1
print(cnt)
