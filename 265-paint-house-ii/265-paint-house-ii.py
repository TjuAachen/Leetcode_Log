from heapq import heapify
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        #find the min and second_min in the previous row
        prev_min_cost = prev_second_min_cost = prev_min_color = None
        for ind, elem in enumerate(costs[0]):
            if prev_min_cost is None or elem < prev_min_cost:
                prev_second_min_cost = prev_min_cost
                prev_min_cost = elem
                prev_min_color = ind
                
            elif (not prev_second_min_cost or elem < prev_second_min_cost):
                prev_second_min_cost = elem
        
        for house in range(1, n):
            min_cost = second_min_cost = min_color = None
            for color in range(k):
                cost = costs[house][color]
                if color == prev_min_color:
                    cost += prev_second_min_cost
                else:
                    cost += prev_min_cost
                if not min_cost or cost < min_cost:
                    second_min_cost = min_cost
                    min_cost = cost
                    min_color = color
                    
                elif not second_min_cost or cost < second_min_cost:
                    second_min_cost = cost
            prev_min_cost = min_cost
            prev_min_color = min_color
            prev_second_min_cost = second_min_cost
        return prev_min_cost
                    
                    
            
                
        