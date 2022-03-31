class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])
        row_ind, col_ind = 0, col - 1
        while(0 <= row_ind < row and 0 <= col_ind < col):
            cur = matrix[row_ind][col_ind]
            if target == cur:
                return True
            elif target < cur:
                col_ind = col_ind - 1
            else:
                row_ind = row_ind + 1
        return False
                
        