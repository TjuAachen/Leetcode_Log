class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.size = list(range(n))
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
    def find (self, x) :
        while( self.parent[x] != x):
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        num = length * (length - 1) // 2
        slope = [-1] * num
        cur = 0
        length = len(points)
        num = length * (length - 1) // 2
        slope = [-1] * num
        cur = 0
        if length <= 1:
            return length
        for ind, point in enumerate(points):
            for j in range(ind+1, length):
                p1, p2 = point, points[j]
                if p2[0] == p1[0]:
                    if p2[1] < p1[1]:
                        slope[cur] = [-float('inf'), ind, j]
                    else:
                        slope[cur] = [float('inf'), ind, j]
                    cur += 1
                    continue
                value = (p2[1] - p1[1]) / (p2[0] - p1[0])
                slope[cur] = [value, ind, j]
                cur += 1

        slope.sort()
        i = 0
        max_length = 0
        while(i < num):
            cur = i
            line = UnionFind(length)
            while(cur < num and slope[cur][0] == slope[i][0]):
                p1, p2 = slope[cur][1], slope[cur][-1]
                line.union(p1,p2)
                cur += 1
            
            i = cur
            cur_length = max(line.size)
            if max_length < cur_length:
                max_length = cur_length
        return max_length
        
                
        