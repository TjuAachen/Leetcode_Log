class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        max_layer = len(triangle)
        dp = [[float('inf') for i in range(row+1)] for row in range(max_layer)]
        dp[0][0] = triangle[0][0]
        for row in range(1,max_layer):
            for col in range(row+1):
                if 1 <= col <= row-1:
                    dp[row][col] = min(dp[row-1][col], dp[row-1][col-1]) + triangle[row][col]
                elif col >= 1:
                    dp[row][col] = dp[row-1][col-1] + triangle[row][col]
                else:
                     dp[row][col] = dp[row-1][col] + triangle[row][col]
        return min(dp[max_layer-1])
        