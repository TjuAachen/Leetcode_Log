class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.nrow, self.ncol = len(matrix) + 1, len(matrix[0]) + 1
        self.BIT = [[0] * self.ncol for _ in range(self.nrow + 1)]
        self.build()
    
    def lowbit(self, num):
        return num&(-num)
    
    def build(self):
        for i in range(1, self.nrow):
            for j in range(1, self.ncol):
                self.point_update(i-1, j - 1, self.matrix[i-1][j-1])
    def point_update(self, row, col, delta):
        i, j = row + 1, col + 1
        while(i < self.nrow):
         #   self.BIT[i][j] += delta
            k = j
            while(k < self.ncol):
                self.BIT[i][k] += delta
                k += self.lowbit(k)
            i += self.lowbit(i)
        
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        delta = val - self.matrix[row][col]
        self.point_update(row, col, delta)
        self.matrix[row][col] = val
    def prefix_sum(self, row, col):
        i, j = row + 1, col + 1
        res = 0
        while(i > 0):
          #  res += self.BIT[i][j]
            k = j
            while(k > 0):
                res += self.BIT[i][k]
                k -= self.lowbit(k)
            i -= self.lowbit(i)
        return res
                
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
       # print(self.BIT)
        r2_c2 = self.prefix_sum(row2, col2)
        r1_c1 = self.prefix_sum(row1 - 1, col1 - 1)
        r1_c2 = self.prefix_sum(row1-1, col2)
        r2_c1 = self.prefix_sum(row2 , col1 - 1)
        return r2_c2 + r1_c1 - r1_c2 - r2_c1
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)