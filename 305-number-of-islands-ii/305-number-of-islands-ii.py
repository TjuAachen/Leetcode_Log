class union_find():
    def __init__(self, n, nrow, ncol):
        self.parent = [-1] * n
        self.size = [0] * n
        self.res = 0
        self.n = ncol
        self.m = nrow
        self.final_parent = set()
        self.coor2num = {}
    def add(self, x, y, node):
        if (x,y) in self.coor2num:
            return len(self.final_parent)
        self.parent[node] = node
        self.size[node] = 1
        self.final_parent.add(node)
        self.coor2num[(x,y)] = node
        diff = [(1,0),(0,1),(-1,0),(0,-1)]
        for dx, dy in diff:
            neigh_x, neigh_y = x + dx, y + dy
            if 0 <= neigh_x < self.m and 0 <= neigh_y < self.n and (neigh_x, neigh_y) in self.coor2num:
                neighbor = self.coor2num[(neigh_x, neigh_y)]
                
                if self.parent[neighbor] != -1:
                    self.union(neighbor, node)
                
        return len(self.final_parent)
    
    
    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    
    def union(self, p, q):
        parent_p, parent_q = self.find(p), self.find(q)
        if parent_p == parent_q:
            return
        if self.size[parent_p] < self.size[parent_q]:
            self.parent[parent_p] = parent_q
            self.final_parent.remove(parent_p)
            self.size[parent_q] += self.size[parent_p]
        else:
            self.parent[parent_q] = parent_p
            self.final_parent.remove(parent_q)
            self.size[parent_p] += self.size[parent_q]
        
class Solution(object):

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        total = len(positions)
        union_set = union_find(total, m, n)
        added = set()
        diff = [(1,0),(0,1),(-1,0),(0,-1)]
        num_of_islands = 0
        res = []
        for ind, position in enumerate(positions):
            x, y = position
            res.append(union_set.add(x,y, ind))
        return res
            

                    
        
                
        
                    
            
            
        