# from collections import deque
import collections
# from heapq import heappop, heappush

n = int(input())
u = [0] * (n)
v = [0] * (n)
w = [0] * (n)

for i in range(1,n):
    u[i], v[i], w[i] = map(int, input().split())

g = collections.defaultdict(list)
for frm, to, distance in zip(u,v,w):
    g[frm].append([to, distance])
    g[to].append([frm, distance])

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

## index でソート
sorted_idx_w = [i[0] for i in sorted(enumerate(w), key=lambda x:x[1], reverse=False)]

un = UnionFind(n+1)
ans = 0
for i in sorted_idx_w[1:]:
    ans += un.size(u[i])*un.size(v[i])*w[i]
    un.union(u[i],v[i])
print(ans)