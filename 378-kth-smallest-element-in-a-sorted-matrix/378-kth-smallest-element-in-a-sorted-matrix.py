class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        def check(mid):
            count = 0
            row, col = n - 1, 0
            smaller, larger = -float('inf'), float('inf')
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1
                else:
                    larger = min(larger, matrix[row][col])
                    row -= 1
            return count, smaller, larger
        left, right = matrix[0][0], matrix[-1][-1]
        
        while(left < right):
            mid = left + (right - left) // 2
            count, smaller, larger = check(mid)
            if count == k:
                return smaller
            elif count > k:
                right = smaller
            else:
                left = larger
        return left
        
        
                    
        