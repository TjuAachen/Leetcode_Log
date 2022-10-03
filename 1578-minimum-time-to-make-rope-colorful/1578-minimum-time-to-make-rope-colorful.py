from heapq import * 
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        #need to be removed
        
        left = 0
        #sliding window
        n = len(colors)
        ans = 0
        while(left < n):
            if left + 1 < n and colors[left + 1] == colors[left]:
                right = left
                heap = []
                curTotal = 0
                curMax = 0
                while(right < n and colors[right] == colors[left]):
                    curMax = max(curMax, neededTime[right])
                    curTotal += neededTime[right]
                    right += 1
                ans += curTotal - curMax
                left = right
            else:
                left += 1
        return ans
                
                
                
        