n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)

def bisec(ok, val):
    ng = n
    # print("ok",ok,"ng",ng)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        # print("ok",ok,"ng",ng,"mid",mid)
        # print(l[mid],val)
        if l[mid] > val:
            ok = mid
        else:
            ng = mid
    # print("ng",ng,"ok",ok)
    return ok

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        # if l[i] == l[j]:
        #     continue
        # print("i",i,"j",j)
        ret = bisec(j,l[i]-l[j])
        cnt += ret-j
        # print("cnt",cnt,"ret",ret)
        # print("cnt",cnt,"i",i,"j",j,"l[i]",l[i],"l[j]",l[j],"bisec",ret)
print(cnt)

# def is_ok(n):
#     # 条件を満たすかどうか？問題ごとに定義
#     return a*n + b*len(str(n)) <= x

# def meguru_bisect(ng, ok):
#     '''
#     初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
#     まずis_okを定義すべし
#     ng ok は  とり得る最小の値-1 とり得る最大の値+1
#     最大最小が逆の場合はよしなにひっくり返す
#     '''
#     while (abs(ok - ng) > 1):
#         mid = (ok + ng) // 2
#         if is_ok(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok

# print(meguru_bisect(10**9 + 1, 0))
