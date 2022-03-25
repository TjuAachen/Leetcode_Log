class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sort_cost = sorted(costs,key = lambda x : x[0] - x[1])
        n = len(sort_cost)//2
        total = 0
        for i in range(n):
            total += sort_cost[i][0]+sort_cost[i+n][1]
        return total
            
            
                
            
        