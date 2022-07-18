class segmentTree():
    def __init__(self, n):
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4*n)
        self.buildTree(1, 0, n-1)
    
    def buildTree(self, node, left, right):
        if left == right:
            return
        mid = left + (right - left) // 2
        self.buildTree(node * 2, left, mid)
        self.buildTree(node * 2 + 1, mid + 1, right)
        self.tree[node] = max(self.tree[node * 2], self.tree[node*2 + 1])
    
    def pushdown(self,node, left, right):
        if self.lazy[node] == 0: return
        self.update_lazy(2 * node, self.lazy[node])
        self.update_lazy(2 * node + 1, self.lazy[node])
        self.lazy[node] = 0
    
    def update_lazy(self, node, lazy):
        self.lazy[node] = max(self.lazy[node],lazy)
        self.tree[node] = max(self.tree[node], self.lazy[node])
    
    def update_range(self, node, left, right, val, l, r):
        if l <= left and right <= r:
            self.update_lazy(node, val)
            return
        if r < left or l > right:
            return
        mid = left + (right - left) // 2
        self.pushdown(node, left, right)
        self.update_range(node * 2, left, mid, val, l, r)
        self.update_range(node * 2 + 1, mid + 1, right, val, l, r)
    def query(self,node, left, right, key):
        if key < left or key > right:
            return 0
        if left == right == key:
            return self.tree[node]
        mid = left + (right - left) // 2
        self.pushdown(node, left, right)
        left = self.query(node * 2, left, mid, key)
        right = self.query(node * 2 + 1, mid + 1, right, key)
        return max(left, right)
    
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        total_points = []
        seen = set()
        x2index = {}
        min_x, max_x = float('inf'), 0
        for index, building in enumerate(buildings):
            x, y, h = building
            if x not in seen:
                total_points.append(x)
                seen.add(x)
            if y not in seen:
                total_points.append(y)
                seen.add(y)
        total_points.sort()
        for index, point in enumerate(total_points):
            x2index[point] = index
        n = len(total_points)
        segment = segmentTree(n)
        for x, y, h in buildings:
            segment.update_range(1, 0, n - 1, h, x2index[x], x2index[y] - 1)
        
        prev_h = None
        res = []
        
        for point in total_points:
            cur_h = segment.query(1, 0, n-1, x2index[point])
            if prev_h == None or prev_h != cur_h:
                prev_h = cur_h
                res.append([point, cur_h])
        return res
            
            
        
        
                    
            
            
            
            
                    

                    
            
        
            
            
                    
            
            
        