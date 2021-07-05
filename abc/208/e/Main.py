n = int(input())
a = list(map(int,input().split()))
mod = 10**9+7

cnt = 0
def dfs(l,x):

    tmp_val = 0
    tmp_cnt = 0
    
    for i in range(len(l)):
        tmp_val += l[i]
        if tmp_val % x == 0:
            tmp_cnt += dfs(l[i+1:],x+i+1)
    print(l,x,tmp_val)
    return tmp_val
cnt = dfs(a,1)
print(cnt)
