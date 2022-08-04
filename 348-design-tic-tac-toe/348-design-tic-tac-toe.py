class TicTacToe:

    def __init__(self, n: int):
        self.matrix = [[0] * n for _ in range(n)]
        self.vertical_sum = [0] * n
        self.horizontal_sum = [0] * n
        self.status = 0
        self.n = n
        self.positive_diagonal_sum = 0
        self.negative_diagonal_sum = 0
    def detect(self, row, col):
        #diagonal
        n = self.n

        if self.positive_diagonal_sum == n or self.negative_diagonal_sum == n:
            return True,1
        if self.positive_diagonal_sum == 101*n or self.negative_diagonal_sum == 101*n:
            return True,2
        #vertical
        if self.vertical_sum[row] == n or self.horizontal_sum[col] == n:
            return True,1
        #horizontal
        if self.vertical_sum[row] == 101*n or self.horizontal_sum[col] == 101*n:
            return True,2
        
        return False,0
    def move(self, row: int, col: int, player: int) -> int:
       # print(row, col, self.status)
        if self.status:
            return self.status
        #self.detect()
        if player == 1:
            self.matrix[row][col] = 1
            self.vertical_sum[row] += 1
            self.horizontal_sum[col] += 1
            if row == col:
                self.positive_diagonal_sum += 1
            if row + col == self.n - 1:
                self.negative_diagonal_sum += 1
        else:
            self.matrix[row][col] = 101
            self.vertical_sum[row] += 101
            self.horizontal_sum[col] += 101   
            if row == col:
                self.positive_diagonal_sum += 101
            if row + col == self.n - 1:
                self.negative_diagonal_sum += 101
                #print(1)
        #print(self.vertical_sum, self.horizontal_sum)
        boolean ,self.status = self.detect(row, col)
        return self.status


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)