class Solution:
    def __init__(self):
        self.prefix = []
        self.MOD = pow(10, 9) + 7
        self.memo = defaultdict(int)
    def buildPrefix(self, pizza):
        nrow, ncol = len(pizza), len(pizza[0])
        self.prefix = [[0] * ncol for _ in range(nrow)]
        for row in range(nrow):
            for col in range(ncol):
                if pizza[row][col] == 'A':
                    self.prefix[row][col] += 1
                if col - 1 >= 0:
                    self.prefix[row][col] += self.prefix[row][col - 1]
                if row - 1 >= 0:
                    self.prefix[row][col] += self.prefix[row - 1][col]
                if col - 1 >= 0 and row - 1>= 0:
                    self.prefix[row][col] -= self.prefix[row - 1][col - 1]     
    def ways(self, pizza: List[str], k: int) -> int:
        self.buildPrefix(pizza)
        nrow, ncol = len(pizza), len(pizza[0])
        return self.result(0, 0, nrow - 1, ncol - 1, k)
    
    def result(self, leftRow, leftCol, rightRow, rightCol, k):
        key = tuple([leftRow, leftCol, rightRow, rightCol, k])
        if key in self.memo:
            return self.memo[key]
        curTotal = self.count(leftRow, leftCol, rightRow, rightCol)
        if curTotal == 0:
            self.memo[key] = 0
            return 0
        if k == 1:
            self.memo[key] = 1
            return 1
        #divide vertically
        res = 0
        for col in range(leftCol, rightCol + 1):
            if self.count(leftRow, leftCol, rightRow, col) != 0:
                res += self.result(leftRow, col + 1, rightRow, rightCol, k - 1)%self.MOD
                res = res%self.MOD
        
        
        #divide horizontally
        for row in range(leftRow, rightRow + 1):
            if self.count(leftRow, leftCol, row, rightCol) != 0:
                res += self.result(row + 1, leftCol, rightRow, rightCol, k - 1)%self.MOD 
                res = res%self.MOD
        self.memo[key] = res%self.MOD
        return res%self.MOD
            
            
    def count(self, leftRow, leftCol, rightRow, rightCol):
        curTotal = self.prefix[rightRow][rightCol]
        up = 0
        left = 0
        middle = 0
        if leftRow > 0:
            up = self.prefix[leftRow - 1][rightCol]
        if leftCol > 0:
            left = self.prefix[rightRow][leftCol - 1]
        if leftCol > 0 and leftRow > 0:
            middle = self.prefix[leftRow - 1][leftCol - 1]
        curTotal = curTotal - up - left
        curTotal += middle
        return curTotal
        
            
        