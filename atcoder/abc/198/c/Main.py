import math
r,x,y = map(int, input().split())

r_2 = math.sqrt(x*x + y*y)

if r_2 == r:
    print(1)
    exit()

if r_2 <= 2*r:
    print(2)
    exit()

print(math.ceil(r_2 /r))

# for i in range(1,141423):
#     if r*r*(i-1)*(i-1) < r_2 and r_2 <= r*r*i*i:
#         print(i)
#         exit()



# def is_ok(i):
#     # 条件を満たすかどうか？問題ごとに定義
#     # if i == 0:
#         # return True

#     # return r*r*(i-1)*(i-1) < r_2 and r_2 <= r*r*i*i
#     return r*r*(i-1)*(i-1) < r_2

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

# print(meguru_bisect(141422 + 1, 0))