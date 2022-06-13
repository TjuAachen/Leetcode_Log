class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]
        nrow = len(triangle)
        for ind1 in range(1, nrow):
            n = len(triangle[ind1])
            dp.append([float('inf') for _ in range(n)])
            for ind2 in range(n):
                if ind2 > 0:
                    dp[-1][ind2] = min(dp[-1][ind2], dp[-2][ind2-1] +triangle[ind1][ind2])
                if ind2 < n - 1:
                    dp[-1][ind2] = min(dp[-1][ind2], dp[-2][ind2] +triangle[ind1][ind2])
        return min(dp[-1])
                        
                
        