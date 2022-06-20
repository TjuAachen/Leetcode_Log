class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        houseNum = len(costs)
        dp = [[float('inf') for _ in range(3)] for _ in range(houseNum)]
        #initial value
        for i in range(3):
            dp[0][i] = costs[0][i]
        for i in range(1, houseNum):
            for j in range(3):
                cur_cost = costs[i][j]
                for k in range(3):
                    if k != j:
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + cur_cost)
                        
        return min(dp[-1])