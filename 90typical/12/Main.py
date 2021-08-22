h, w = map(int, input().split())
q = int(input())
qz = [list(map(int, input().split())) for _ in range(q)]
mass = [[False for _ in range(w+1)] for _ in range(h+1)]

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

un = UnionFind(4*10**7+1)
for i in range(q):
    if qz[i][0] == 1:
        x_ = qz[i][1]
        y_ = qz[i][2]
        for j in ((x_+1,y_),(x_,y_+1),(x_-1,y_),(x_,y_-1)):
            if j[0] <= 0 or j[1] <= 0 or j[0] > h or j[1] > w:
                continue
            if mass[j[0]][j[1]]:
                # print(qz[i][1],qz[i][2],qz[i][3],qz[i][4])
                un.union(x_*w+y_,j[0]*w+j[1])
        # print("x",x,"y",y)
        mass[x_][y_] = True
    else:
        if not mass[qz[i][1]][qz[i][2]] and qz[i][1] == qz[i][3] and qz[i][2] == qz[i][4]:
            print("No")
            continue
        # print(qz[i][1],qz[i][2],qz[i][3],qz[i][4])
        if mass[qz[i][1]][qz[i][2]] and un.same(qz[i][1]*w+qz[i][2],qz[i][3]*w+qz[i][4]):
            print("Yes")
        else:
            print("No")
