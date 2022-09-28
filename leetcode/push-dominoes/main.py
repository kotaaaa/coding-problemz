class Solution:
    def cmp(self, a, b):
        if a > b:
            return 1
        elif a == b:
            return 0
        else:
            return -1

    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != "."]
        symbols = [(-1, "L")] + symbols + [(len(dominoes), "R")]

        print("symbols", symbols)
        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            print((i, x), (j, y))
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i + 1, j):
                    ans[k] = ".LR"[self.cmp(k - i, j - k)]

        return "".join(ans)
