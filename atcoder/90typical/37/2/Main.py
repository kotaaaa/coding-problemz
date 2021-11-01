W, N = map(int, input().split())
S = [map(int, input().split()) for _ in range(N)]

INF = 10 ** 16
DEFAULT = -INF   # クエリーの初期値
QUERY = max      # クエリーの種類

class SegmentTree:
    def __init__(self, N):
        self.sz = 2 ** (N - 1).bit_length()
        self.dat = [DEFAULT] * self.sz * 2

    def update(self, l, r, x):   # 木の構築をまとめて行う
        if type(x) in [int, float]:
            x = [x] * (r - l)
        l += self.sz - 1
        r += self.sz - 1
        self.dat[l: r] = x
        while 0 < l < r:
            l = (l - 1) // 2
            r = r // 2
            for i in range(l, r):
                self.dat[i] = QUERY(self.dat[i * 2 + 1], self.dat[i * 2 + 2])

    def query(self, l, r):
        l += self.sz - 1
        r += self.sz - 1
        res = DEFAULT
        while l < r:
            res = QUERY(res, self.dat[l])
            res = QUERY(res, self.dat[r - 1])
            l = l // 2
            r = (r - 1) // 2
        return res

dp = [-INF] * (W + 1)
dp[0] = 0
seg = SegmentTree(W)
# print(seg.query(0,10))
# print(seg.query(10,20))
# print(seg.query(1,2))
# print(seg.query(3,8))
# print(seg.query(3,7))
# print(seg.query(3,6))
# exit()

seg.update(0, 1, 0)

for L, R, V in S:
    # print("dp",dp)
    print("seg.dat",seg.dat)
    for w in range(L, R):
        dp[w] = max(dp[w], seg.query(0, w - L + 1) + V)
    for w in range(R, W + 1):
        dp[w] = max(dp[w], seg.query(w - R, w - L + 1) + V)
    seg.update(0, W + 1, dp)

print(dp[W] if dp[W] > 0 else -1)