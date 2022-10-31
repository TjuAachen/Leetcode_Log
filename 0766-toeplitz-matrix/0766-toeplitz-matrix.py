class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #diagonal line
        nrow, ncol = len(matrix), len(matrix[0])
        
        totalNum = nrow + ncol - 1
        
        for diff in range(-totalNum, totalNum):
            prevNum = None
            for row in range(nrow):
                col = row - diff
                if col < ncol and col >= 0:
                    curNum = matrix[row][col]
              #      print(prevNum, curNum, diff)
                    if prevNum != None and curNum != prevNum:
                        return False
                    prevNum = curNum
        return True
            
        