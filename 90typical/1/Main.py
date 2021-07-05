#########################
# 二分探索, binary search
#########################
# ok ,,, ng > left: ok, right: ng (最大値を求める) < 典型01
# ng ,,, ok > left: ng, right: ok (最小値を求める) < ABC203d
n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

def solve(mid):
    """ ある羊羹の切れ目の間隔の最小値候補が条件を満たすか否かを判定する
    Args:
        mid (int): [羊羹の切れ目の間隔の最小値候補]
    Returns:
        boolean: [判定対象のindex が条件を満たすかどうか]
    """
    tmp_val = 0 # 切った羊羹の長さ
    cut_cnt = 0 # 羊羹を切る数
    for i in range(n):
        if a[i] - tmp_val >= mid and l - a[i] >= mid:
            cut_cnt += 1
            tmp_val = a[i]
    if cut_cnt >= k:
        return True
    else:
        False
right = l
left = 0
while right - left > 1:
    mid = (right + left) // 2
    if solve(mid): # 条件を満たす
        left = mid
    else: # 条件を満たさない
        right = mid
print(left)