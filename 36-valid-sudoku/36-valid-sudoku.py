class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def validate(s):
            res = [0] * 9
            for char in s:
                if '1'<= char <= '9':
                    res[int(char)-1] += 1
            if max(res) != 0 and max(res) > 1:
                return False
            return True
        for row in board:
            if not validate(row):
                return False
        for col in range(9):
            if not validate([board[l][col] for l in range(9)]):
                return False
        for k in range(9):
            stack = []
            for i in range(k%3*3,3*(k%3+1)):
                for j in range(k//3*3,k//3*3+3):
                    stack.append(board[i][j])
            if not validate(stack):
                return False
        return True
                
            
        