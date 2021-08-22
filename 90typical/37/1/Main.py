w, n = map(int, input().split())
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    l[i], r[i], v[i] = map(int, input().split())

### SegMent Tree ###
## ref: https://qiita.com/takayg1/items/c811bd07c21923d7ec69
#####segfunc#####
def segfunc(x, y):
    return max(x, y)
#################

#####ide_ele#####
# ide_ele =
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

# seg = SegTree([45,3,2,46,34,41,64,25,53,24],segfunc,0)
# print(seg.query(1,2))
# print(seg.query(3,8))
# print(seg.query(3,7))
# print(seg.query(3,6))
# exit()

dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, w+1):
        ## i番目の料理を作るとき, i番目の料理を作らないとき
        # if j >= l[i]:
        seg = SegTree(dp[i - 1], segfunc, 0)
        dp[i][j] = max(seg.query(j - r[i], j - l[i] + 1) + v[i], dp[i - 1][j])
        ## まだ一つも料理を作っていないとき
        # else:
        #     dp[i][j] = dp[i - 1][j]
print(dp)
print(len(dp),len(dp[0]))
print(dp[n - 1][w - 1])
