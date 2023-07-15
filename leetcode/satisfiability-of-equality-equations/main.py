# https://leetcode.com/problems/satisfiability-of-equality-equations/submissions/
#  Union find
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if x >= self.n:
            return -1
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        v = UnionFind(27)
        vals = {}
        for i in equations:
            if i[1] == "!":
                continue
            v.union(ord(i[0]) - 97, ord(i[3]) - 97)

        for i in equations:
            if i[1] != "!":
                continue
            if v.same(ord(i[0]) - 97, ord(i[3]) - 97):
                return False
        return True
