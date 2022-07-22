class union_find:
    def __init__(self,n):
        self.size = [1] * n
        self.parent = [i for i in range(n)]
    def union(self, p, q):
        parent_p, parent_q = self.find(p), self.find(q)
        if parent_p == parent_q:
            return
        if self.size[parent_p] < self.size[parent_q]:
            self.parent[parent_p] = parent_q
            self.size[parent_q] += self.size[parent_p]
        else:
            self.parent[parent_q] = parent_p
            self.size[parent_p] += self.size[parent_q]
    def find(self, p):
        if self.parent[p] == p:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_set = union_find(n)
        for x, y in edges:
            union_set.union(x, y)
        num_set = set()
        for i in range(n):
            parent = union_set.find(i)
            if parent not in num_set:
                num_set.add(parent)
        return len(num_set)
            
            
            
        