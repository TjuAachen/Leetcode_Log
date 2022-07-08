class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf') for _ in range(target+1)] for _ in range(n)] for _ in range(m)]
        total_cost = 0
        #modify in the original house array
        for i in range(m):
            cur = -1
            if houses[i] != 0:
                cur = houses[i] - 1
            if cur != -1 and i == 0:
                dp[i][cur][target-1] = 0
                continue
            for j in range(n):
                #same with the previous predefined
                if i > 0 and cur != -1 and j == cur:
                    for k in range(target+1):
                        dp[i][cur][k] = min(dp[i][cur][k], dp[i-1][cur][k])
                #not same with the previous predefined
                elif i > 0 and j  != cur and cur != -1:
                    for k in range(1, target+1):
                        dp[i][cur][k-1] = min(dp[i][cur][k-1], dp[i-1][j][k])
                elif i > 0 and cur == -1:
                    for t in range(n):
                        for k in range(target+1):
                            if j == t:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k] + cost[i][j])
                            elif k > 0:
                                dp[i][j][k-1] = min(dp[i][j][k-1], dp[i-1][t][k] + cost[i][j])
                elif i == 0:
                    dp[i][j][target-1] = min(dp[i][j][target-1],cost[i][j])    
        res = float('inf')
        for j in range(n):
            res = min(res, dp[-1][j][0])
      #  print(dp)
        if res != float('inf'):
            return res
        return -1
                        
                    
                