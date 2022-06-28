from heapq import heapify
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [[float('inf') for _ in range(k)] for _ in range(n)]
        #except k, the minimum cost
        temp = costs[0][:]
        heapify(temp)
        for i in range(k):
            if costs[0][i] == temp[0]:
                popped = heappop(temp)
                dp[0][i] = temp[0]
                heappush(temp,popped)
            else:
                dp[0][i] = temp[0]
        
        for i in range(1,n):
            temp = [dp[i-1][j] + costs[i][j] for j in range(k)]
            heapify(temp)
            for j in range(k):
                if dp[i-1][j] + costs[i][j] == temp[0]:
                    popped = heappop(temp)
                    dp[i][j] = temp[0]
                    heappush(temp,popped)
                else:
                    dp[i][j] = temp[0]
            
        return min(dp[-1])