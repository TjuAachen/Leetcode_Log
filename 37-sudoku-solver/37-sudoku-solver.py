import copy
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def available(i,j):
            row = set([m for m in board[i] if m != "."])
            col = set([board[k][j] for k in range(9) if board[k][j] != "."])
            block = set()
            for m in range(i//3*3,i//3*3+3):
                for n in range(j//3*3,j//3*3+3):
                    if board[m][n] != ".":
                        block.add(board[m][n])
            final = row.union(col)
            final = final.union(block)
            stack = []
            for i in range(1,10):
                if str(i) not in final:
                    stack.append(i)
            return stack
        undecided = dict()
        n = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    undecided[n] = (i,j)
                    n = n + 1
        total_num = len(undecided)
        def backtracking(n):
            global res
            if n == total_num:
                return True
            point = undecided[n]
            i, j = point[0],point[1]
            nums = available(i, j)
            if not nums:
                return False
            for num in nums:
                board[i][j] = str(num)
                if backtracking(n+1):
                    return True
                board[i][j] = "."
        backtracking(0)
        return board
                
            
                    
        