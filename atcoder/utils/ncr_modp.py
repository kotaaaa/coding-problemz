class ncr_modp:
    # ncr mod p 参考: https://drken1215.hatenablog.com/entry/2018/06/08/210000
    max = 10 ** 6 + 1
    mod = 10 ** 9 + 7
    fac = [0 for _ in range(max)]
    finv = [0 for _ in range(max)]
    inv = [0 for _ in range(max)]
    #  テーブルを作る前処理
    def __init__(self):
        self.fac[0] = 1
        self.fac[1] = 1
        self.finv[0] = 1
        self.finv[1] = 1
        self.inv[1] = 1
        for i in range(2, self.max):
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.inv[i] = self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    # 二項係数計算
    def cmb(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * (self.finv[k] * self.finv[n - k] % self.mod) % self.mod


# 計算例
ncr = ncr_modp()
print(ncr.cmb(100000, 50000))
