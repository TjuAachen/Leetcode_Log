class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.nrow, self.ncol = len(self.matrix), len(self.matrix[0])
        self.prefix = [[0] * self.ncol for _ in range(self.nrow)]
        self.build_prefix()
        
    def build_prefix(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                if j == 0:
                    self.prefix[i][j] = self.matrix[i][j]
                else:
                    self.prefix[i][j] = self.matrix[i][j] + self.prefix[i][j-1]
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                ans += self.prefix[i][col2]
            else:
                ans += self.prefix[i][col2] - self.prefix[i][col1 - 1]
        return ans
            
                
        
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)