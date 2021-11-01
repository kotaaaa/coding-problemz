#########################
## Seg木　セグ木: 
## https://algo-logic.info/segment-tree/
## https://qiita.com/toast-uz/items/bf6f142bace86c525532
#########################

w, n = map(int, input().split())
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
v = [0 for _ in range(n)]
for i in range(n):
    l[i], r[i], v[i] = map(int, input().split())


class SegTree:
    def __init__(self, arr) -> None:
        self.init_val = -1
        self.arr_n = len(arr)
        self.n = 2 ** (self.arr_n - 1).bit_length()
        self.dat = [self.init_val] * (self.n * 2 - 1)

        for i in range(self.arr_n):
            self.dat[self.n - 1 + i] = arr[i]
        for i in range(self.n - 2, 0, -1):
            self.dat[i] = max(self.dat[2*i+1],self.dat[2*i+2])


    def update(self, i, x):
        i += self.n - 1
        self.dat[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.dat[i] = max(self.dat[2 * i + 1], self.dat[2 * i + 2])

    def query(self, a, b):
        return self.query_sub(a, b, 0, 0, self.n)

    def query_sub(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.init_val
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            v1 = self.query_sub(a, b, 2 * k + 1, l, (l + r) // 2)
            v2 = self.query_sub(a, b, 2 * k + 2, (l + r) // 2, r)
            return max(v1, v2)

# inf = 10**10
dp = [[-1 for _ in range(w+1)] for _ in range(n+1)]
dp[0][0] = 0
seg = SegTree([-1 for _ in range(w+1)])
seg.update(0,0)

for i in range(n):
    for j in range(w+1):
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        cl = max(0, j-r[i])
        cr = max(0, j-l[i]+1)
        if cl == cr:
            continue
        val = seg.query(cl,cr)
        if val == -1:
            continue
        dp[i+1][j] = max(dp[i+1][j], val+v[i])
    seg = SegTree(dp[i+1])
        
if dp[n][w] == 0:
    print(-1)
else:
    print(dp[n][w])





