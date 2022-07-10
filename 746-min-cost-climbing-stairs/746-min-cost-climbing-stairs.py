class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n+1)]
        cost.append(0)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,n+1):
            prev, prev_prev = float('inf'), float('inf')
            if i > 0:
                prev = dp[i-1] 
            if i > 1:
                prev_prev = dp[i-2]
            dp[i] = min(prev,prev_prev) + cost[i]
        return min(dp[-1], dp[-2])