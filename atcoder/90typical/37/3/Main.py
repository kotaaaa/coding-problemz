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
        self.init_val = 0
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

# seg = SegTree([10,9,8,7,6,5,4,3,20,1])
# print(seg.query(4, 10))
# print(seg.query(4, 9))
# print(seg.query(4, 8))
inf = 10**10
dp = [[-inf for _ in range(w+1)] for _ in range(n+1)]
# dp = [0 for _ in range(n+1)]
seg = SegTree([0 for _ in range(w+1)])
for i in range(1,n+1):
    # for j in range(1,w+1):
    #     dp[i][j] = dp[i-1][j]
    # for j in range(1,w+1):
        
    #     cl = max(0, j-r[i-1])
    #     cr = max(0, j-l[i-1]+1)
 
    #     if cl == cr:
    #         continue
        # if j - l[i-1] < 0: # or j - r[i-1] > 0:
        #     dp[i][j] = dp[i-1][j]
        #     continue
        # if j - r[i-1] > 0:
        #     dp[i][j] = max(dp[i][j - r[i-1]] + v[i-1], dp[i-1][j])
        #     continue
        # print(i,j,l[i-1],r[i-1],"seg.query(j-r[i],j-l[i]+1)",seg.query(min(0,j-r[i-1]),j-l[i-1]+1))
        # val = seg.query(max(0,j-r[i-1]),j-l[i-1]+1)
        # val = seg.query(cl,cr)
        # if val == -inf:
        #     continue
        # dp[i][j] = max(dp[i-1][j], val+v[i-1])
    # for w in range(l[i-1], r[i-1]):
    #     dp[w] = max(dp[w], seg.query(0, w - l[i-1] + 1) + v[i-1])
    # for w in range(r[i-1], w[i-1] + 1):
    #     dp[w] = max(dp[w], seg.query(w - r[i-1], w - l[i-1] + 1) + v[i-1])
    print("dp[i]",dp[i])
    seg = SegTree(dp[i])
        
# print(len(dp),len(dp[0]))
# print(dp)
if dp[n][w] == 0:
    print(-1)
else:
    print(dp[n][w])





