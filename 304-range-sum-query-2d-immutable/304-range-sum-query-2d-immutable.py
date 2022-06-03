class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.nrow, self.ncol = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.prefix = [[0] * (self.ncol + 1) for _ in range(self.nrow + 1)]
        self.build_prefix()
        
        
        
    def build_prefix(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                self.prefix[i + 1][j + 1] = self.prefix[i + 1][j] + self.prefix[i][j + 1] + self.matrix[i][j] - self.prefix[i][j]
                
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.prefix[row2 + 1][col2 + 1]  + self.prefix[row1][col1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)