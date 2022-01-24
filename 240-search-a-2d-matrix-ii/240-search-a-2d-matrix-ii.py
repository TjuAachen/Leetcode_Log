class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        l, r = 0, len(matrix[0]) 
        while(l < r):
            mid = (l+r)//2
            if matrix[0][mid] == target:
                return True
            elif matrix[0][mid] > target:
                r = mid
            else:
                l = mid + 1
        col = l - 1
        for i in range(col+1):
            l, r = 0, len(matrix) - 1
            while(l <= r):
                mid = (l + r) // 2
                if matrix[mid][i] == target:
                    return True
                elif matrix[mid][i] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
        
            
        