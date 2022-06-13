class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nrow = len(triangle)
        for ind1 in range(1, nrow):
            n = len(triangle[ind1])
            for ind2 in range(n):
                temp = triangle[ind1][ind2]
                triangle[ind1][ind2] = float('inf')
                if ind2 > 0:
                    triangle[ind1][ind2] = min(float('inf'),triangle[ind1-1][ind2-1] +temp)
                if ind2 < n - 1:
                    triangle[ind1][ind2] = min(triangle[ind1][ind2],triangle[ind1-1][ind2] + temp)
        return min(triangle[-1])
                        
                
        