# ncr mod p 参考: https://drken1215.hatenablog.com/entry/2018/06/08/210000
x, y = map(int, input().split())

if (x + y) % 3 != 0:
    print(0)
    exit()


max = 10 ** 6 + 1
mod = 10 ** 9 + 7

fac = [0 for _ in range(max)]
finv = [0 for _ in range(max)]
inv = [0 for _ in range(max)]

#  テーブルを作る前処理
def COMinit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

# 二項係数計算
def COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


# 前処理
COMinit()
# 計算例
# print(COM(100000, 50000))
a = (2 * x - y) // 3
b = (2 * y - x) // 3
print(COM(a+b, a))
