class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nrow, ncol = len(matrix), len(matrix[0])
        
        i, j = 0, ncol - 1
        
        while(0 <= i < nrow and 0 <= j < ncol):
            cur = matrix[i][j]
            if cur == target:
                return True
            if cur < target:
                i = i + 1
            else:
                j = j - 1
           # print(i,j, cur)
        return False
                
        
            
        