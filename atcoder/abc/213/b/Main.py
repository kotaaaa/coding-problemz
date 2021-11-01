n = int(input())
a = list(map(int,input().split()))

a_idx = [i[0] for i in sorted(enumerate(a), key=lambda x:x[1],reverse=True)]
# print(a_idx)
print(a_idx[1]+1)