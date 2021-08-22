# w, n = map(int, input().split())
# l = [0 for _ in range(n)]
# r = [0 for _ in range(n)]
# v = [0 for _ in range(n)]
# for i in range(n):
#     l[i], r[i], v[i] = map(int, input().split())


class SegTree:
    def __init__(self, n) -> None:
        self.inf = 10 ** 10
        # self.n = n
        self.n = 2 ** (n - 1).bit_length()
        self.dat = [self.inf] * (self.n * 2 - 1)
        # self.dat = [self.inf] * (2 * n - 1)

    def update(self, i, x):
        i += self.n - 1
        self.dat[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.dat[i] = min(self.dat[2 * i + 1], self.dat[2 * i + 2])

    def query(self, a, b):
        return self.query_sub(a, b, 0, 0, self.n)

    def query_sub(self, a, b, k, l, r):
        print("a, b, k, l, r ", a, b, k, l, r)
        if r <= a or b <= l:
            return self.inf
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            v1 = self.query_sub(a, b, 2 * k + 1, l, (l + r) // 2)
            v2 = self.query_sub(a, b, 2 * k + 2, (l + r) // 2, r)
            print("v1,v2",v1,v2)
            return min(v1, v2)

seg = SegTree(10)
print("seg.dat", seg.dat)
for i in range(10):
    seg.update(i, 10 - i)
print("seg.dat", seg.dat)
# for i in range(1, 10):
#     print("i", i)
#     print(seg.query(0, i))
print(seg.query(4, 9))
