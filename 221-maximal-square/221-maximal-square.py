class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rowNum, colNum = len(matrix), len(matrix[0])
        
        dp = [[0] * colNum for _ in range(rowNum)]
        max_res = 0
        for i in range(colNum):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                max_res = 1
        
        for i in range(rowNum):
            if matrix[i][0] == '1':
                dp[i][0] = 1      
                max_res = 1
        
        for row in range(1, rowNum):
            for col in range(1, colNum):
                prev = min([dp[row-1][col-1],dp[row][col-1],dp[row-1][col]])
                if matrix[row][col] == '1':
                    dp[row][col] = prev + 1
                else:
                    dp[row][col] = 0
                
                max_res = max(dp[row][col], max_res)
        return max_res**2
            