class union_find:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.size = [1] * n
    def union(self, i, j):
        parentI, parentJ = self.find(i), self.find(j)
        if parentI == parentJ:
            return
        if self.size[parentI] > self.size[parentJ]:
            self.size[parentI] += self.size[parentJ]
            self.parent[parentJ] = parentI
        else:
            self.size[parentJ] += self.size[parentI]
            self.parent[parentI] = parentJ            
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        n = len(vals)
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)
        union_set = union_find(n)
        ans = 0
        valToIdx = defaultdict(list)
        #start from 0
        for i, val in enumerate(vals):
            valToIdx[val].append(i)
        
        for val in sorted(valToIdx.keys()):
            for idx in valToIdx[val]:
                for nxt in neighbors[idx]:
                    if vals[nxt] <= vals[idx]:
                        union_set.union(nxt, idx)
            countOfConnected = defaultdict(int)
            for idx in valToIdx[val]:
                countOfConnected[union_set.find(idx)] += 1
            
            for x in countOfConnected.values():
                ans += x + x*(x-1) // 2
            
        return ans
            
            
            
            