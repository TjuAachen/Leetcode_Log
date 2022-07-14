class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nrow, self.ncol = len(matrix), len(matrix[0])
        self.tree = [[0 for _ in range(4*self.nrow)] for _ in range(4*self.ncol)]
        self.matrix = matrix
        self.buildTree(1, 1, 0, self.ncol -1, 0, self.nrow - 1)
    
    def buildTree(self, row, col, left, right, up, down):
        if left == right and up == down:
            self.tree[row][col] = self.matrix[up][left]
            return
        mid1, mid2 = left + (right - left) // 2, up + (down - up) // 2
        if left != right and up != down:
            self.buildTree(2*row, 2* col, left, mid1, up, mid2)
            self.buildTree(2*row + 1, 2* col,mid1 + 1, right, up, mid2)
            self.buildTree(2*row + 1, 2* col + 1, mid1 + 1, right, mid2 + 1, down)
            self.buildTree(2*row, 2* col + 1, left, mid1, mid2+1, down)
            self.tree[row][col] = self.tree[2*row+1][2*col] + self.tree[2*row][2*col] + self.tree[2*row][2*col+1] + self.tree[2*row+1][2*col+1]
        elif left == right and up != down:
            self.buildTree(row, 2* col, left, right, up, mid2)
            self.buildTree(row, 2* col + 1, left, right, mid2 + 1, down)
            self.tree[row][col] = self.tree[row][2*col] + self.tree[row][2*col + 1]
        elif left != right and up == down:
            self.buildTree(2*row, col, left, mid1, up, down)
            self.buildTree(2*row + 1, col,mid1 + 1, right, up, down)
            self.tree[row][col] = self.tree[2*row][col] + self.tree[2*row + 1][col]       
    def point_update(self, row, col, left, right, up, down, r, c, val):
        if left == right == c and up == down == r:
            self.tree[row][col] = val
            self.matrix[r][c] = val
            return
        if c < left or c > right or r < up or r > down:
            return
        mid1, mid2 = left + (right - left) // 2, up + (down - up) // 2
        if left != right and up != down:
            self.point_update(2*row, 2* col, left, mid1, up, mid2, r, c, val)
            self.point_update(2*row + 1, 2* col,mid1 + 1, right, up, mid2, r, c, val)
            self.point_update(2*row + 1, 2* col + 1, mid1 + 1, right, mid2 + 1, down, r, c, val)
            self.point_update(2*row, 2* col + 1, left, mid1, mid2+1, down, r, c, val)
            self.tree[row][col] = self.tree[2*row+1][2*col] + self.tree[2*row][2*col] + self.tree[2*row][2*col+1] + self.tree[2*row+1][2*col+1]
        elif left == right and up != down:
            self.point_update(row, 2* col, left, right, up, mid2, r, c, val)
            self.point_update(row, 2* col + 1, left, right, mid2 + 1, down, r, c, val)
            self.tree[row][col] = self.tree[row][2*col] + self.tree[row][2*col + 1]
        elif left != right and up == down:
            self.point_update(2*row, col, left, mid1, up, down, r, c, val)
            self.point_update(2*row + 1, col,mid1 + 1, right, up, down, r, c, val)
            self.tree[row][col] = self.tree[2*row][col] + self.tree[2*row + 1][col] 

    def update(self, row: int, col: int, val: int) -> None:
        self.point_update(1, 1, 0, self.ncol - 1, 0, self.nrow - 1, row, col, val)
    
    def enquiry(self, row, col, left, right, up, down, row1, col1, row2, col2):
        if col1 <= left and right <= col2 and row1 <= up and down <= row2:
            return self.tree[row][col]
        
        mid1, mid2 = left + (right - left) // 2, up + (down - up) // 2
        if right < col1 or col2 < left or row2 < up or down < row1:
            return 0 
        ans = 0
        if left != right and up != down:
            ans += self.enquiry(2*row, 2* col, left, mid1, up, mid2,row1, col1, row2, col2)
            ans += self.enquiry(2*row + 1, 2* col,mid1 + 1, right, up, mid2,row1, col1, row2, col2)
            ans += self.enquiry(2*row + 1, 2* col + 1, mid1 + 1, right, mid2 + 1, down,row1, col1, row2, col2)
            ans += self.enquiry(2*row, 2* col + 1, left, mid1, mid2+1, down,row1, col1, row2, col2)
        elif left == right and up != down:
            ans += self.enquiry(row, 2* col, left, right, up, mid2,row1, col1, row2, col2)
            ans += self.enquiry(row, 2* col + 1, left, right, mid2 + 1, down,row1, col1, row2, col2)
        elif left != right and up == down:
            ans += self.enquiry(2*row, col, left, mid1, up, down,row1, col1, row2, col2)
            ans += self.enquiry(2*row + 1, col,mid1 + 1, right, up, down,row1, col1, row2, col2)            
        return ans
            
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.enquiry(1, 1, 0, self.ncol - 1, 0, self.nrow -1, row1, col1, row2, col2)
    
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)