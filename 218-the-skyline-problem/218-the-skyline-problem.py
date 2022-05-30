class segment:
    def __init__(self, buildings):
        self.temp1= {}
        self.temp = []
        self.cor2ind = {}
        self.ind2cor = {}
        self.heights = []
        for building in buildings:
            x, y, h = building
            if x in self.temp1:
                self.temp1[x] = max(self.temp1[x], h)
            else:
                self.temp1[x] = h
            if y in self.temp1:
                self.temp1[y] = max(self.temp1[y], 0)
            else:
                self.temp1[y] = 0
        for key, val in self.temp1.items():
            self.temp.append([key, val])
        self.temp.sort()
        n = len(self.temp)
        self.tree = [0] * 4 * n
        self.lazy = [0] * 4 * n
        for ind,elem in enumerate(self.temp):
            self.cor2ind[elem[0]] = ind
            self.ind2cor[ind] = elem[0]
            self.heights.append(elem[1])
        self.build(1, 0, n - 1)
        
    def build(self, root, l, r):
        if (l == r): 
            self.tree[root] = self.temp[l][1]
            return
        mid = l + (r - l) // 2
        self.build(2 * root, l, mid)
        self.build(2 * root + 1, mid + 1, r)
        self.tree[root] = max(self.tree[2 * root], self.tree[2 * root + 1])
        
    
    def update(self, root, l, r, height, ql, qr):

        if (self.lazy[root] != 0):
            self.tree[root] = max(self.lazy[root], self.tree[root])
            #for non-leaf node, then update its children
            if (l != r):
                self.lazy[2 * root] = max(self.lazy[root], self.lazy[2 * root])
                self.lazy[2 * root + 1] = max(self.lazy[root], self.lazy[2 * root + 1])
            self.lazy[root] = 0
        #out of range
        if(r < ql or qr < l):
            return
        # fully within the range
        if (ql <= l and r <= qr):
            self.tree[root] = max(self.tree[root], height)
            if(l != r):
                self.lazy[2 * root] = max(height, self.lazy[2 * root])
                self.lazy[2 * root + 1] = max(height, self.lazy[2 * root + 1])
            return
        mid = l + (r - l) // 2
        self.update(2 * root, l, mid, height, ql, qr)
        self.update(2 * root + 1, mid + 1, r, height, ql, qr)
        self.tree[root] = max(self.tree[2 * root], self.tree[2 * root + 1])
        
    def query(self, root, l, r, index):
        if ( index < l or index > r):
            return -1
        if self.lazy[root] != 0:
            self.tree[root] = max(self.tree[root], self.lazy[root])
            if (l != r):
                self.lazy[2 * root] = max(self.lazy[root], self.lazy[2 * root])
                self.lazy[2 * root + 1] = max(self.lazy[root], self.lazy[2 * root + 1])
            self.lazy[root] = 0
            
        if ( l == r and index == l):
            return self.tree[root]
        mid = l + (r - l) // 2
        left = self.query(2 * root, l, mid, index)
        right = self.query(2 * root + 1, mid + 1, r, index)
        if left != -1:
            return left
        return right
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        tree = segment(buildings)
        n = len(tree.temp)
        for building in buildings:
            ql, qr, height = building
            indl, indr = tree.cor2ind[ql], tree.cor2ind[qr]
            tree.update(1, 0, n - 1, height, indl, indr - 1)
        final = []
        i = 0
        heights = []
        for j in range(n):
            heights.append(tree.query(1, 0, n-1, j))
        
        while(i < n):
            final.append([tree.ind2cor[i],heights[i]])
            j = i
            while(j < n and heights[j] == heights[i]):
                j = j + 1
            i = j
        return final
                    
            
            
            
            
                    

                    
            
        
            
            
                    
            
            
        