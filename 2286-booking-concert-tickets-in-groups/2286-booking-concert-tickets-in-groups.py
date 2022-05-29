class segment:
    def __init__(self, n, m):
        self.nrow = n
        self.nseat = m
        self.tree = [0] * (4 * n)
        self.max = [0] * (4 * n)
        self.build_tree(1, 0, n - 1)
    def build_tree(self, root, l, r):
        if (l == r):
            self.tree[root] = self.nseat
            self.max[root] = self.nseat
            return
        mid = l + (r - l) // 2
        self.build_tree(root * 2, l, mid)
        self.build_tree(root * 2 + 1, mid + 1, r)
        self.tree[root] = self.tree[root * 2] + self.tree[root * 2 + 1]
        self.max[root] = max(self.max[root * 2], self.max[root * 2 + 1])
    
    def update(self, root, l, r, index, value):
        if (l == r and l == index):
            self.tree[root] = value
            self.max[root] = value
            return
        if (index < l or index > r): return
        mid = l + (r - l) // 2
        self.update(root * 2, l, mid, index, value)
        self.update(root * 2 + 1, mid + 1, r, index, value)
        self.tree[root] = self.tree[root * 2] + self.tree[root * 2 + 1]
        self.max[root] = max(self.max[root * 2], self.max[root * 2 + 1])
    
    def gather_query(self, root, l, r, k, maxRow):
        if ( l == r and l <= maxRow and self.tree[root] >= k):
            res = self.tree[root]
            self.update(1, 0, self.nrow - 1, l, self.tree[root] - k)
            return [l, self.nseat - res]
        if (l == r):
            return []
        if (self.max[root] < k): return []
        mid = l + (r - l) // 2
        if self.max[2*root] >= k:
            return self.gather_query(2 * root, l, mid, k, maxRow)
        return self.gather_query(2 * root + 1, mid + 1, r, k, maxRow)
    
    def sum_query(self, root, l, r, ql, qr):
        if (l >= ql and r <= qr): return self.tree[root]
        if (ql > r or qr < l): return 0
        mid = l + (r - l) // 2
        return self.sum_query(root * 2, l, mid, ql, qr) + self.sum_query(root * 2 + 1, mid + 1, r, ql, qr)
    
        
        
        
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.tree = segment(n, m)
        self.nseat = m
        self.nrow = n
        self.seat = [m] * n
        

    def gather(self, k: int, maxRow: int) -> List[int]:
        res = self.tree.gather_query(1, 0, self.nrow - 1, k, maxRow)
        if res:
            [row, start] = res
            self.seat[row] = self.seat[row] - k
            return [row, start]
        return []

        
    def scatter(self, k: int, maxRow: int) -> bool:
        total = self.tree.sum_query(1, 0, self.nrow - 1, 0, maxRow)
        if total < k:
            return False
        for i in range(maxRow + 1):
            res = self.seat[i]
            if res == 0:
                continue
            if res < k:
                self.seat[i] = 0
                self.tree.update(1, 0, self.nrow - 1, i, 0)
                k = k - res
            else:
                self.seat[i] = self.seat[i] - k
                self.tree.update(1, 0, self.nrow - 1, i, res - k)
                break
        return True
                
            

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)