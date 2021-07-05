# class UnionFind():
#     def __init__(self, n):
#         self.n = n
#         self.parents = [-1] * n

#     def find(self, x):
#         if self.parents[x] < 0:
#             return x
#         else:
#             self.parents[x] = self.find(self.parents[x])
#             return self.parents[x]

#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)

#         if x == y:
#             return

#         if self.parents[x] > self.parents[y]:
#             x, y = y, x

#         self.parents[x] += self.parents[y]
#         self.parents[y] = x

#     def size(self, x):
#         return -self.parents[self.find(x)]

#     def same(self, x, y):
#         return self.find(x) == self.find(y)

#     def members(self, x):
#         root = self.find(x)
#         return [i for i in range(self.n) if self.find(i) == root]

#     def roots(self):
#         return [i for i, x in enumerate(self.parents) if x < 0]

#     def group_count(self):
#         return len(self.roots())

#     def all_group_members(self):
#         return {r: self.members(r) for r in self.roots()}

#     def __str__(self):
#         return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


# v = UnionFind(10)
# # print(v.parents,v.all_group_members().values())
# # v.union(1,3)
# # print(v.parents,v.all_group_members().values())
# # v.union(4,5)
# # print(v.parents,v.all_group_members().values())
# # v.union(1,5)
# # print(v.parents,v.all_group_members().values())

# # v.union(1,2)
# # v.union(2,3)
# print(v.all_group_members().values())
# # v.union(1,3)
# v.union(1,1)
# print(v.all_group_members().values())
# print(v.group_count())


class Node:
    def __init__(self):
        self.parent = -1
        self.children = []

def cal_depth(node_id, d = 0):
    Tree[node_id].depth = d
    for child in Tree[node_id].children:
        cal_depth(child, d+1)
    
N = int(input())
p = list(map(int,input().split()))
Tree = [Node() for _ in p]

q = int(input())
ud = [map(int, input().split()) for _ in range(q)]
u,d = [list(i) for i in zip(*ud)]

print(Tree)
