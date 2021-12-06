################################
### LIS 最長増加部分列 (二分探索で) ##
################################

n = int(input())
a = list(map(int,input().split()))

p = [0 for _ in range(n+1)]
q = [0 for _ in range(n+1)]

def lis(x, arr):
    b = [10**9 for _ in range(len(x)+1)] # 記録用配列
    b[0] = 0 ##左端に 0 を追加しておく，調べる値は0より大きいことは確定
    b[1] = x[0] ## 配列の最初の値は，無条件に入れる．
    arr[1] = 1 ## 配列の最初なので，部分列の長さは１
    len_b = 1 ## 最長増加部分列の長さ (これをbのindexとしてそのまま使える．なぜならbの初期値に0が含まれているから)
    for i in range(1,len(x)):
        ## 二分探索 ##
        left = 0 ## ok の最小値
        right = len_b + 1 ## ngの最小値
        while left + 1 < right:
            mid = (left + right) // 2
            if b[mid] < x[i]: #targetが配列のある要素(b[mid])よりも大きい配列のindexを求めたい
                left = mid 
            else:
                right = mid
        b[left+1] = x[i] ## x[i]が最大となる最長増加部分列を保持するように記録用配列を更新
        arr[i+1] = left+1 ## i地点での最長増加部分列をメモ 
        len_b = max(len_b,left+1) ## 最長増加部分列の長さを更新
        # print("left",left,"arr",arr,"b",b,"len_b",len_b)

lis(a,p)
a.reverse()
lis(a,q)
q.reverse()

ans = 0
for i in range(n):
    ans = max(ans,p[i+1] + q[i] - 1)
print(ans)