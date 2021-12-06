#########################
## Seg木　セグ木 セグメント木，他の人の解法
## https://algo-logic.info/segment-tree/
## https://qiita.com/toast-uz/items/bf6f142bace86c525532
#########################

w, n = map(int, input().split())
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    l[i], r[i], v[i] = map(int, input().split())

class SegmentTree(object):
    __slots__ = ["elem_size", "tree", "default", "op"]
 
    def __init__(self, a: list, default: int, op):
        from math import ceil, log
        real_size = len(a)
        self.elem_size = elem_size = 1 << ceil(log(real_size, 2))
        self.tree = tree = [default] * (elem_size * 2)
        tree[elem_size:elem_size + real_size] = a
        self.default = default
        self.op = op
 
        for i in range(elem_size - 1, 0, -1):
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])
 
    def get_value(self, x: int, y: int) -> int:  # 半開区間
        l, r = x + self.elem_size, y + self.elem_size
        tree, result, op = self.tree, self.default, self.op
        while l < r:
            if l & 1:
                result = op(tree[l], result)
                l += 1
            if r & 1:
                r -= 1
                result = op(tree[r], result)
            l, r = l >> 1, r >> 1
 
        return result
 
    def set_value(self, i: int, value: int) -> None:
        k = self.elem_size + i
        self.tree[k] = value
        self.update(k)
 
    def update(self, i: int) -> None:
        op, tree = self.op, self.tree
        while i > 1:
            i >>= 1
            tree[i] = op(tree[i << 1], tree[(i << 1) + 1])


dp = [[-1 for _ in range(w+1)] for _ in range(n+1)]
dp[0][0] = 0
seg = SegmentTree([-1]*(w+1), -1, max)
seg.set_value(0,0)

for i in range(n):
    for j in range(w+1):        
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        cl = max(0, j-r[i])
        cr = max(0, j-l[i]+1)
        if cl == cr:
            continue
        val = seg.get_value(cl,cr)
        if val == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j], val+v[i])
    for j in range(w+1):
        seg.set_value(j,dp[i+1][j])
        
if dp[n][w] == 0:
    print(-1)
else:
    print(dp[n][w])





