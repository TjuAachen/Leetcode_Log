class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0] * (n+2) for _ in range(m+2)] for _ in range(maxMove + 1)]
        #initial value
        dp[0][startRow+1][startColumn+1] = 1
        
        diff = [(1,0), (0, -1), (0, 1), (-1, 0)]
        for i in range(maxMove):
            for row in range(1,m+1):
                for col in range(1,n+1):
                    if dp[i][row][col] != 0:
                        for dx, dy in diff:
                            newx, newy = row + dx, col + dy
                            if 0 <= newy < n+2 and 0 <= newx < m+2:
                                dp[i+1][newx][newy] += dp[i][row][col]
            #boundary
            for row in range(m+2):
                dp[i+1][row][0] += dp[i][row][0]
                dp[i+1][row][-1] += dp[i][row][-1]
            for col in range(n+2):
                dp[i+1][0][col] += dp[i][0][col]
                dp[i+1][-1][col] += dp[i][-1][col]               
        ans = 0
        for row in range(m+2): 
            ans += dp[-1][row][0]
            ans += dp[-1][row][-1]
        for col in range(n+2):
            ans += dp[-1][0][col]
            ans += dp[-1][-1][col] 
        return ans%(10**9+7)
            
            
            
                        
                    
        